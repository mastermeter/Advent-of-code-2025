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

def mix_range():
    idx = 0
    while idx<len(input)-1:
        if input[idx][0] == input[idx+1][0]:
            if input[idx][1]<=input[idx+1][1]:
                input.pop(idx)
            else :
                input.pop(idx+1)
        elif input[idx+1][1] >= input[idx][1] >= input[idx+1][0]:
            input[idx][1]=input[idx+1][1]
            input.pop(idx+1)
        elif input[idx][1]==input[idx+1][0]-1:
            input[idx][1]=input[idx+1][1]
            input.pop(idx+1)
        elif input[idx][1] > input[idx+1][1]:
            input.pop(idx+1)
        else:
            idx += 1
    return input

input = preprocess_data()
input = sorted(input, key=lambda x: x[0])

for i in range(len(input)-1):
    if input[i][0]>input[i+1][0]:
        print(False)

input = mix_range()

for i in range(len(input)-1):
    if input[i][0]>input[i+1][0]:
        print(False)

print(input)
s=0
for r in input:
    a=r[1]-r[0]+1
    s+=a

print(s, s==354226555270043)