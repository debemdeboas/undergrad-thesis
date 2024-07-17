from pathlib import Path

import modal
import modal.gpu
from modal import Image

MODEL_NAME = "meta-llama/Meta-Llama-3-70B-Instruct"
MODEL_REVISION = "main"
MODEL_DIR = f"/models/{MODEL_NAME}"
# CACHE_PATH = "/root/cache"


def download_model():
    import os

    from huggingface_hub import snapshot_download

    os.makedirs(MODEL_DIR, exist_ok=True)

    snapshot_download(
        MODEL_NAME,
        local_dir=MODEL_DIR,
        ignore_patterns=["*.pt", "*.bin"],
        revision=MODEL_REVISION,
    )


image = (
    Image.debian_slim(python_version="3.10")
    .pip_install(
        "vllm==0.5.1",  # LLM serving
        "huggingface_hub",  # download models from the Hugging Face Hub
        "hf-transfer",  # download models faster
        "bitsandbytes",  # for quantization
        "transformers",
        "accelerate",
    )
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "1"})
    .run_function(
        download_model,
        secrets=[modal.Secret.from_name("hf_token")],
    )
    .pip_install(
        "transformers==4.41.2",
        "vllm==0.5.0",
    )
)

app = modal.App("vllm-openai-compatible")

N_GPU = 2
TOKEN = "super-secret-token"
local_template_path = Path(__file__).parent / "template_llama3.jinja"

GPU_CONFIG = modal.gpu.A100(count=N_GPU, size="80GB")


@app.cls(
    image=image,
    gpu=GPU_CONFIG,
    container_idle_timeout=20 * 60,  # 20 minutes
    mounts=[modal.Mount.from_local_file(local_template_path, remote_path="/root/chat_template.jinja")],
    secrets=[modal.Secret.from_name("hf_token")],
)
class Model:
    @modal.build()
    def build(self):
        # from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
        # import transformers.utils

        # quantization_config = BitsAndBytesConfig(load_in_8bit=True, llm_int8_enable_fp32_cpu_offload=True)

        # model = AutoModelForCausalLM.from_pretrained(
        #     MODEL_DIR, use_cache=True, device_map="auto", quantization_config=quantization_config
        # )
        # tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR, use_cache=True, use_fast=True)

        # model.save_pretrained(CACHE_PATH, safe_serialization=False)
        # tokenizer.save_pretrained(CACHE_PATH, safe_serialization=False)

        # transformers.utils.move_cache()
        pass

    @modal.enter()
    async def aenter(self):
        import time

        import fastapi
        import fastapi.middleware
        import fastapi.middleware.cors
        import vllm.entrypoints.openai.api_server as api_server
        from vllm.engine.arg_utils import AsyncEngineArgs
        from vllm.engine.async_llm_engine import AsyncLLMEngine
        from vllm.entrypoints.openai.serving_chat import OpenAIServingChat
        from vllm.entrypoints.openai.serving_completion import (
            OpenAIServingCompletion,
        )
        from vllm.usage.usage_lib import UsageContext

        print("🥶 cold starting inference...")
        start = time.monotonic_ns()

        engine_args = AsyncEngineArgs(
            model=MODEL_DIR,
            tensor_parallel_size=GPU_CONFIG.count,
            gpu_memory_utilization=1.0,
            max_model_len=4096,
            disable_log_stats=True,
            disable_log_requests=True,
            enforce_eager=False,  # capture the graph for faster inference, but slower cold starts (30s > 20s)
        )

        self.engine = AsyncLLMEngine.from_engine_args(engine_args, usage_context=UsageContext.OPENAI_API_SERVER)
        model_config = await self.engine.get_model_config()

        duration_s = (time.monotonic_ns() - start) / 1e9
        print(f"🏎️ engine started in {duration_s:.0f}s")

        self.api = api_server.app
        # security: CORS middleware for external requests
        self.api.add_middleware(
            fastapi.middleware.cors.CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # security: auth middleware
        @self.api.middleware("http")
        async def authentication(request: fastapi.Request, call_next):
            if not request.url.path.startswith("/v1"):
                return await call_next(request)
            if request.headers.get("Authorization") != "Bearer " + TOKEN:
                return fastapi.responses.JSONResponse(content={"error": "Unauthorized"}, status_code=401)
            return await call_next(request)

        api_server.openai_serving_chat = OpenAIServingChat(
            self.engine,
            model_config=model_config,
            served_model_names=[MODEL_DIR],
            response_role="assistant",
            lora_modules=[],
            chat_template="chat_template.jinja",
        )

        api_server.openai_serving_completion = OpenAIServingCompletion(
            self.engine, model_config=model_config, served_model_names=[MODEL_DIR], lora_modules=[]
        )

    @modal.asgi_app()
    def serve(self):
        return self.api
