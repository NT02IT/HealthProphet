class TrainingData():
    conv = None
    def __init__(self, url, name = "Traning"):
        self.url = str(url)
        self.name = str(name)
        self.conv = open(url, 'r', encoding='UTF-8')
    def __str__(self):
        return self.name
    
    def toList(self):
        conv_list = self.conv.readlines()
        result = []
        temp = []
        for item in conv_list:
            if item != "\n":
                temp.append(item)
            else:
                result.append(temp)
                temp = []
        if len(temp) > 0:
            result.append(temp)
        return result
    
    def close(self):
        self.conv.close()