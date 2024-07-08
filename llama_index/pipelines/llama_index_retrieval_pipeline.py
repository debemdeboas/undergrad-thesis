"""
title: Llama Index RAG Pipeline
author: debemdeboas
date: 2024-07-01
version: 1.0
license: MIT
description: This pipeline uses the LlamaIndex library to retrieve documents from a knowledge base. 
requirements: llama-index, llama-index-llms-ollama, llama-index-embeddings-ollama, llama-index-embeddings-huggingface, llama-index-llms-groq, llama-index-llms-vllm, einops, accelerate, transformers, llama-index-llms-openai-like httpx torch
"""

import logging
import os
import sys
from typing import Generator, Iterator, Literal, Union

import httpx
import torch
from pydantic import BaseModel

from llama_index.core import (
    Settings,
    SimpleDirectoryReader,
    VectorStoreIndex,
    load_index_from_storage,
)
from llama_index.core.base.llms.types import ChatMessage
from llama_index.core.chat_engine import CondensePlusContextChatEngine
from llama_index.core.chat_engine.types import BaseChatEngine
from llama_index.core.indices.base import BaseIndex
from llama_index.core.node_parser import HierarchicalNodeParser, MarkdownNodeParser
from llama_index.core.storage import StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq
from llama_index.llms.ollama import Ollama
from llama_index.llms.openai_like import OpenAILike

logging.basicConfig(
    stream=sys.stdout, level=logging.WARN, format="[%(filename)s:%(lineno)s - %(funcName)s() ] %(message)s"
)


class Pipeline:
    class Valves(BaseModel):
        """
        Configuration options for the pipeline.
        These options can be set through the OpenWebUI interface.
        """

        temperature: float = 0.5

        hf_token: str = ""

        embed_model: str = "BAAI/bge-m3"  # nomic-ai/nomic-embed-text-v1.5
        embed_model_trust_remote_code: bool = False
        embed_cuda: bool = False

        llm_provider: Literal["ollama", "groq", "openailike"] = "ollama"

        ollama_base_url: str = "http://localhost:11434"
        ollama_model: str = "llama3:70b-instruct-q8_0"

        groq_api_key: str = ""
        groq_model: str = "llama3-70b-8192"

        oai_like_api_base: str = ""
        oai_like_api_key: str = ""
        oai_like_model: str = ""

        system_prompt: str = (
            "Act as a teacher assistant and answer questions using the provided context.\n"
            "Your goal is to help students and teachers by providing cohesive and correct responses based on educational material, while applying guided learning techniques. Give examples and cite the context whenever possible.\n"
            "Don't mention 'according to the context' or anything related to that, ever.\n\n"
            "## Instructions\n"
            "1. External Information: Use external information from the vector database to answer questions. Select the most relevant and reliable information available.\n"
            "2. Guided Learning Techniques: Avoid giving direct answers. Instead, guide the user through the learning process, encouraging critical thinking and discovery.\n"
            "3. Coherent and Correct Responses: Ensure that all responses are coherent and correct, strictly following the educational material provided.\n"
            "4. Inference Capability: Use your skills to accurately deduce and infer information.\n"
            "5. User-Friendly Interface: Be easy to use and access. Provide clear and well-structured responses suitable for a web interface.\n"
            "6. Value Addition: Add value for both students and teachers. Offer useful insights, pedagogical guidance, and support the teaching-learning process.\n"
            "7. Best-effort: The user is a beginner, and may use terms incorrectly or in other languages. Do your best to understand what they mean.\n\n"
            "## User Interaction\n"
            "- Interactive Guidance: Ask the user if they would like more details or additional examples.\n"
            "- Encourage Exploration: Motivate users to explore more about the topic by suggesting additional resources or related questions.\n\n"
            "## Additional Information\n"
            "- Utilize the context provided in the vector database to enrich your responses.\n"
            "- Ensure your answers are always up-to-date and based on the most recent information available.\n\n"
            "Your mission is to provide a rich and interactive learning experience, helping students and teachers achieve their educational goals efficiently and effectively.\n"
        )

        learning_analytics_api: str = ""

    index: BaseIndex
    documents: list
    engine: BaseChatEngine
    storage_context: StorageContext

    def __init__(self):
        logging.debug("Initializing pipeline...")
        self.valves = self.Valves()

    async def on_startup(self):
        logging.info("Startup...")

        logging.info(f"CUDA available: {torch.cuda.is_available()}")

        await self.on_valves_updated()

        logging.info("Configuring embedding model...")
        Settings.embed_model = HuggingFaceEmbedding(
            self.valves.embed_model,
            trust_remote_code=self.valves.embed_model_trust_remote_code,
            device="cuda" if self.valves.embed_cuda else "cpu",
        )
        logging.debug(Settings.embed_model)

        logging.info("Checking for persistent data...")
        self.persist_dir = "/app/persist/"
        if os.path.exists(self.persist_dir + "docstore.json"):
            logging.info("Loading index from storage...")
            self.storage_context = StorageContext.from_defaults(persist_dir=self.persist_dir)
            self.index = load_index_from_storage(self.storage_context)
        else:
            logging.info("Loading documents and creating index...")
            self.storage_context = StorageContext.from_defaults()
            self.documents = SimpleDirectoryReader("/app/rag-data/").load_data()
            self.storage_context.docstore.add_documents(self.documents)
            self.index = VectorStoreIndex.from_documents(
                self.documents,
                storage_context=self.storage_context,
                transformations=[
                    MarkdownNodeParser(include_metadata=False),
                    HierarchicalNodeParser.from_defaults(chunk_sizes=[2048, 512, 128], chunk_overlap=30),
                ],
            )

            logging.info("Persisting index...")
            self.storage_context.persist(self.persist_dir)

        logging.info("Configuring chat engine...")
        self.engine = CondensePlusContextChatEngine.from_defaults(
            self.index.as_retriever(),
            context_prompt=self.valves.system_prompt
            + (
                "Here are the relevant documents for the context:\n"
                "{context_str}"
                "\nInstruction: Use the previous chat history, and the context above, to interact and help the user."
                "\nPlease answer in the same language as the question."
            ),
        )
        logging.debug(self.engine)

    async def on_shutdown(self):
        logging.info("Shutdown. Persisting data...")
        self.storage_context.persist(persist_dir=self.persist_dir)

    async def on_valves_updated(self):
        logging.info("Updating valves...")
        logging.debug(self.valves)

        match self.valves.llm_provider:
            case "ollama":
                Settings.llm = Ollama(
                    model=self.valves.ollama_model,
                    base_url=self.valves.ollama_base_url,
                    system_prompt=self.valves.system_prompt,
                    temperature=self.valves.temperature,
                )
            case "groq":
                Settings.llm = Groq(
                    model=self.valves.groq_model,
                    api_key=self.valves.groq_api_key,
                    system_prompt=self.valves.system_prompt,
                )
            case "openailike":
                Settings.llm = OpenAILike(
                    model=self.valves.oai_like_model,
                    api_base=self.valves.oai_like_api_base,
                    api_key=self.valves.oai_like_api_key,
                    system_prompt=self.valves.system_prompt,
                    temperature=self.valves.temperature,
                )

        os.environ["HF_TOKEN"] = self.valves.hf_token

    async def inlet(self, body: dict, user: dict) -> dict:
        logging.debug(f"inlet:{__name__}")

        logging.debug(body)
        logging.debug(user)

        return body

    async def outlet(self, body: dict, user: dict) -> dict:
        logging.debug(f"outlet:{__name__}")

        logging.debug(body)
        logging.debug(user)

        if self.valves.learning_analytics_api:
            try:
                async with httpx.AsyncClient(follow_redirects=True) as client:
                    response = await client.patch(
                        self.valves.learning_analytics_api + f"/api/{user['id']}",
                        json={
                            "name": user["name"],
                        },
                    )
                    response.raise_for_status()
                    logging.debug(response)

                    last_sys_msg = body["messages"][-1]
                    # Sanity check the response
                    if last_sys_msg["role"] != "assistant":
                        logging.warn("Skipping learning analytics API call")
                    else:
                        response = await client.post(
                            self.valves.learning_analytics_api + f"/api/{user['id']}/messages/",
                            json={
                                "content": body["messages"][-2]["content"],
                                "response": last_sys_msg["content"],
                            },
                        )
                        response.raise_for_status()
                        logging.debug(response)
            except Exception as e:
                logging.exception(e)

        return body

    def pipe(
        self, user_message: str, model_id: str, messages: list[dict], body: dict
    ) -> Union[str, Generator, Iterator]:
        logging.debug(
            {
                "user_message": user_message,
                "model_id": model_id,
                "body": body,
                "self.engine": self.engine,
                "Settings.llm": Settings.llm,
                "self": self,
            }
        )

        response = self.engine.stream_chat(user_message, chat_history=self.dict_to_chatmessages(messages))
        return response.response_gen

    @staticmethod
    def dict_to_chatmessages(messages: list[dict[str, str]]) -> list[ChatMessage]:
        return [ChatMessage(**msg) for msg in messages]
