# 🧠 Offline Mistral Chatbot

An offline, privacy-respecting chatbot powered by the Mistral 7B Instruct model in GGUF format. Runs locally using llama-cpp-python, with both command-line and graphical interfaces for interaction. No internet connection required after setup.

---

## 🚀 Features

- ✅ Offline LLM Chatting
- 🧠 Mistral 7B Instruct (Quantized GGUF)
- 💬 Command Line & GUI (Tkinter) modes
- 🖥️ Cross-platform: Windows, Linux, macOS
- 🔒 Private & Secure – no data sent to cloud

---

## 📁 Project Structure

offline-chatbot/
├── chatbot.py # Command-line chatbot
├── gui.py # GUI using Tkinter
├── requirements.txt # Python dependencies
├── mistral-7b-instruct-v0.1.Q4_0.gguf # Mistral model file
└── README.md # This documentation

---

## 📥 Download the Model

You must manually download the quantized Mistral 7B model in GGUF format.

🔗 Hosted on Hugging Face:  
https://huggingface.co/MUPPALAM/mistral

⬇️ Direct model link (4.1 GB):  
https://huggingface.co/MUPPALAM/mistral/resolve/main/mistral-7b-instruct-v0.1.Q4_0.gguf

🗂️ Place the file in the project folder:


---

---

## 💻 Setup

1. Clone the repository:

```bash
git clone https://github.com/prem90902304/offline-chatbot.git
cd offline-chatbot

