def preprocess_data():
    input = []
    file = open("test.txt","r")
    data = file.read().split("\n")
    for i in range(len(data)):
        data[i] = data[i].split(",")
    return data

print(preprocess_data())