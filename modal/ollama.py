from modal import App, Image, web_server, gpu

GPU_CONFIG = gpu.A100(count=1, size="80GB")


def download_model():
    import subprocess
    import requests

    subprocess.Popen("ollama serve", shell=True)

    # Wait for server to come online
    while True:
        try:
            requests.get("http://localhost:11434")
            break
        except requests.exceptions.ConnectionError:
            pass

    subprocess.Popen("ollama pull llama3:70b-instruct-q8_0", shell=True).wait()


image = (
    Image.debian_slim(python_version="3.11")
    .apt_install("curl", "gawk", "grep", "sed", "coreutils", "findutils", "pciutils")
    .run_commands("curl -fsSL https://ollama.com/install.sh | sh", gpu=GPU_CONFIG)
    .pip_install("requests")
    .env({"OLLAMA_HOST": "0.0.0.0"})
    .run_function(download_model, gpu=GPU_CONFIG)
)

app = App("ollama", image=image)


@app.function(gpu=GPU_CONFIG, allow_concurrent_inputs=100, timeout=3600)
@web_server(port=11434, startup_timeout=180)
def run():
    import os
    import subprocess
    import requests

    print("received request")
    my_env = os.environ.copy()
    my_env["OLLAMA_HOST"] = "0.0.0.0"
    my_env["OLLAMA_HTTPS_PROXY"] = "https://debemdeboas-tcc--ollama-run.modal.run"
    my_env["OLLAMA_HTTP_PROXY"] = "http://debemdeboas-tcc--ollama-run.modal.run"

    subprocess.Popen("ollama serve", shell=True, env=my_env)

    # Wait for server to come online
    while True:
        try:
            requests.get("http://localhost:11434")
            break
        except requests.exceptions.ConnectionError:
            pass

    subprocess.Popen('ollama run llama3:70b-instruct-q8_0 ""', shell=True, env=my_env).wait()
