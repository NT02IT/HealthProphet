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
            'default_response': 'Xin lỗi tôi không biết câu trả lời cho vấn đề bạn đang gặp phải T_T',
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
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

#Run flask
if __name__ == "__main__":
    app.run(debug=True, port=5500)