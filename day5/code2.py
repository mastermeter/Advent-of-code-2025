def preprocess_data():
    input = []
    file = open("input.txt","r")
    data = file.read().split("\n\n")
    for i in range(len(data)):
        data[i] = data[i].split("\n")
    for i in range(len(data[0])):
        data[0][i] = data[0][i].split("-")
    for i in data:
        for j in range(len(i)):
            if type(i[j])==list:
                for k in range(len(i[j])):
                    i[j][k]=int(i[j][k])
            else:
                i[j]=int(i[j])
    
                    
    return data[0]

input = preprocess_data()

print(input)

a = set()

for i in input:
    print(i[0]," ",i[1])
print(len(a))