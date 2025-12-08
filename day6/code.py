def preprocess_data():
    input = []
    file = open("test.txt","r")
    data = file.read().split("\n")
    for i in range(len(data)):
        data[i]=list(data[i])
    
                    
    return data

input = preprocess_data()

for i in input:
    print(i)

l = len(input[0])
L = len(input)


t = []
for i in range(l):
    print('0')
    c=[]
    for j in range(L,0):
        n=""
        if input[j][i]=="*":
            print("1")
            a = 1
            for k in c:
                a*=int(k)
        elif input[j][i]=="+":
            print('2')
            a = 0
            for k in c:
                a+=int(k)
        else:
            print('3')
            if input[j][i]=='':
                pass
            else:
                n+=input[j][i]
        print(n)

        
    
        


        
        
    
            
            
