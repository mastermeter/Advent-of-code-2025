def preprocess_data():
    list = []
    file = open("test.txt", "r")
    for line in file:
        list.append(line.replace("\n",""))
    return list

data = preprocess_data()
print(data)
L = len(data[0])
print(L)
def find_biggest_num():
    c = 0
    for n in data:
        print(n[1:13])
    return c

print(find_biggest_num())
