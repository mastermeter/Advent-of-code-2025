def preprocess_data():
    input = []
    file = open("test.txt","r")
    data = file.read().split(",")
    for i in range(len(data)):
        data[i] = data[i].split("-")
    for i in data:
        for j in range(int(i[0]),int(i[1])+1):
            input.append(j)
    return data

input = preprocess_data()

def find_patern(input):
    c = 0
    for i in input:
        s = str(i)
        print(s)
        for j in range(1,len(s)//2):
            #print(s[:j], " ", s)
            if check_subpatern(s[:j],s):
                c+=i
                break
    return c
            


def check_subpatern(patern,string):
    lp = len(patern)
    ls = len(string)
    for i in range(ls//lp):
        #print(string[i*lp:(i+1)*lp], " ", patern)
        if string[i*lp:(i+1)*lp]!=patern:
            return False
    return True

                

print(find_patern(input))

#print(check_subpatern('212','2121212118'))