from llama_cpp import Llama

llm = Llama(
    model_path="./models/mistral-7b-instruct-v0.1.Q4_0.gguf",
    n_ctx=2048,
    n_threads=8,
    n_gpu_layers=20
)

SYSTEM_PROMPT = "You are a helpful AI assistant that answers all types of questions accurately and simply."

def ask_bot(history, user_input):
    full_prompt = f"[INST] <<SYS>>\n{SYSTEM_PROMPT}\n<</SYS>>\n"
    for msg in history[-4:]:
        full_prompt += f"{msg['role']}: {msg['content']}\n"
    full_prompt += f"user: {user_input} [/INST]"

    response = llm(full_prompt, stop=["</s>"], max_tokens=512)
    return response["choices"][0]["text"].strip()
