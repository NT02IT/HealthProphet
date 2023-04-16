import datasheet
import os  
os.system('cls') 

conv = open(r"trainingdata\conversations.txt", 'a+', encoding='UTF-8')
print("---------------CONVERSATIONS---------------")
print(r"| + Nhập 'end' để kết thúc                |")
print(r"| + Nhập 'new' để tạo cuộc trò chuyện mới |")
print("-------------------------------------------")
while True:
    question = input("<?> ")
    if question == "new": 
        print("-------------NEW CONVERSATIONS-------------")
        print(r"| + Nhập 'end' để kết thúc                |")
        print(r"| + Nhập 'new' để tạo cuộc trò chuyện mới |")
        print("-------------------------------------------")
        conv.write("\n")
        continue
    if question == "end":
        conv.write("\n")
        break
    conv.write("\n" + question)
    answer = input(">>> ")
    conv.write("\n" + answer)
conv.close()

#Xem lại kết quả trong file
conv1 = datasheet.TrainingData(r"trainingdata\conversations.txt", "training")
num = 1
for i in conv1.toList():
    print("\nCONVERSATION {}:".format(num))
    print(i)
    num = num + 1