def data_preprocess():
    list = []
    file = open("input.txt", "r")
    for line in file:
        if line[0] == 'L':
            list.append(int("-"+line[1:]))
        else :
            list.append(int(line[1:]))
    file.close()
    return list
input = data_preprocess()

n = 50
n2 = 50
c = 0

print(n2)
for i in input:
    n2 += i
    if n2 == 0:
        print("increased c by + 1")
        c+=1
    elif n2 < 0 and n != 0:
        c+=1*abs(n2//100)
        print(f"increased c by + {abs(n2//100)}")

        n2%=100
    elif n2 < 0 :
        n2%=100
    elif n2 > 99:
        c+=1*abs(n2//100)
        print(f"increased c by + {abs(n2//100)}")
        n2%=100
    print(n2)
    n = n2
print(c)
    