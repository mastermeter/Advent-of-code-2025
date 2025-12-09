def preprocess_data():
    input = []
    file = open("input.txt","r")
    data = file.read().split("\n")
    for i in range(len(data)):
        data[i] = data[i].split(",")
    return data

input = preprocess_data()
print(input)

g = 0

def find_area():
    global g
    for i in range(len(input)-1):
        for j in range(i+1,len(input)):
            a = abs(int(input[i][0])-int(input[j][0])+1)*abs(int(input[i][1])-int(input[j][1])+1)
            if a > g:
                g = a
    return g 

print(find_area())