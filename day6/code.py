def preprocess_data():
    input = []
    file = open("input.txt","r")
    data = file.read().split("\n")
    for i in range(len(data)):
        data[i]=data[i].split()
    
                    
    return data

input = preprocess_data()

print(input)

l = len(input[0])
L = len(input)


t = []
for i in range(l):
    c=[]
    for j in range(L):
        if input[j][i]=="*":
            a = 1
            for k in c:
                a*=int(k)
        elif input[j][i]=="+":
            a = 0
            for k in c:
                a+=int(k)
        else:
            c.append(input[j][i])
    t.append(a)
print(sum(t))

        
    
        


        
        
    
            
            
