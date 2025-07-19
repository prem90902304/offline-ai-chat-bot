import tkinter as tk
from chatbot import ask_bot

history = []

def on_submit():
    user_input = entry.get()
    if not user_input.strip():
        return
    history.append({"role": "user", "content": user_input})
    output.insert(tk.END, f"You: {user_input}\n")

    response = ask_bot(history, user_input)
    history.append({"role": "assistant", "content": response})
    output.insert(tk.END, f"Bot: {response}\n\n")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Offline AI Chatbot")
output = tk.Text(root, wrap=tk.WORD, height=20, width=70)
output.pack()
entry = tk.Entry(root, width=70)
entry.pack()
submit_btn = tk.Button(root, text="Ask", command=on_submit)
submit_btn.pack()
root.mainloop()
