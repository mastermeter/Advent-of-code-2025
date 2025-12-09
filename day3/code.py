def preprocess_data():
    list = []
    file = open("test.txt", "r")
    for line in file:
        list.append(line.replace("\n",""))
    return list

data = preprocess_data()
print(data)

L = 12

