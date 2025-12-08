def preprocess_data():
    input = []
    file = open("input.txt","r")
    data = file.read().split("\n")
    return data

input = preprocess_data()

depth = len(input)

print(len(input[0]))
s = [0 for i in range(len(input[0]))]

def origin():
    for i in range(len(input[0])):
        if input[0][i]=='S':
            print(i)
            return i
a = origin()

s[a]=1

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j]=='^':
            s[j-1]+=s[j]
            s[j+1]+=s[j]
            s[j]=0
    print(s)

print(sum(s))


