from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import handling.datasheet as datasheet

chatbot = ChatBot("HealthProphet")
trainer = ListTrainer(chatbot)

data = datasheet.TrainingData(r"trainingdata\conversations.txt", "trainingdata")
for i in data.toList():
    trainer.train(i)
data.close()