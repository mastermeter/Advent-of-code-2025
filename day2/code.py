def preprocess_data():
    input = []
    file = open("test.txt","r")
    data = file.read().split(",")
    for i in range(len(data)):
        data[i] = data[i].split("-")
    print(data)
    for i in data:
        for j in range(int(i[0]),int(i[1])+1):
            input.append(j)
    print(input)
    return data

input = preprocess_data()

def find_patern(input):
    c = 0
    for i in input:
        s = str(i)
        for j in range(len(s)):
            print(s[:j])
    return c
            

    return c

def check_subpatern(patern,string):
    lp = len(patern)
    ls = len(string)
    for i in range(ls//lp):
        print(string[i*lp:(i+1)*lp], " ", patern)
        if string[i*lp:(i+1)*lp]!=patern:
            return False
    return True

                

print(find_patern(input))

#print(check_subpatern('212','2121212118'))