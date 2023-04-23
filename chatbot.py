from flask import Flask, render_template, request
from chatterbot import ChatBot

app = Flask(__name__)

#Khởi tạo chatbot
chatbot = ChatBot(
    'HealthProphet',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Xin lỗi tôi không biết câu trả lời cho vấn đề bạn đang gặp phải 😥',
            'maximum_similarity_threshold': 0.75
        }
    ]
)

#Trả về trang response.html
@app.route("/response")
def response():
    return render_template("response.html")

#Trả về trang home - index.html
@app.route("/home")
def home():
    return render_template("index.html")

#Nhận và reply tin nhắn
chatbot_response = ""
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    chatbot_response = str(chatbot.get_response(userText))
    return chatbot_response

@app.route("/next")
def get_bot_suggest():
    beforeResponse = request.args.get('chatbot_response')
    return str(chatbot.get_response(beforeResponse))

#Run flask
if __name__ == "__main__":
    app.run(debug=True, port=5500)