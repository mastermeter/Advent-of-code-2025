def data_preprocess():
    list = []
    file = open("test.txt", "r")
    for line in file:
        if line[0] == 'L':
            list.append(int("-"+line[1:]))
        else :
            list.append(int(line[1:]))
    file.close()
    return list
input = data_preprocess()

n2 = 50
c = 0

print(n2)
for i in input:
    n2 += i

    if  n2 < 0 or n2 > 99:
        c+=abs(n2//100)
        print("Increase by", abs(n2//100))
    elif n2 == 0:
        c+=1
        print("Increase by 1")
    n2%=100
    print(n2)
print(c)