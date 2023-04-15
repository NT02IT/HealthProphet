from flask import Flask, render_template, request
from chatterbot import ChatBot

app = Flask(__name__)

chatbot = ChatBot(
    'HealthProphet',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Xin lỗi tôi không biết câu trả lời cho vấn đề bạn đang gặp phải T_T',
            'maximum_similarity_threshold': 0.75
        }
    ]
)

@app.route("/response")
def response():
    return render_template("response.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True, port=5500)

