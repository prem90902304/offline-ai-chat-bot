from flask import Flask, request, jsonify, render_template
from chatbot import ask_bot

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = ask_bot(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
