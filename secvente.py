x = int(input())
list=[]
for i in range(x):
    y=float(input())
    list.append(y)

prag=float(input())
list2=[]
for i in list:
    if i>prag:
        list2.append(1)
    else:
        list2.append(0)

print(list2)

def count_seq(lista):
    kontor = 0
    kontor_0=0
    kontor_1=0
    oneSeen = False
    if lista[0]== 0 and lista[-1] == 1:
        for i in range(len(lista)):
            if lista[i] == 0:
                oneSeen = True
            if lista[i] == 1 and oneSeen:
                kontor += 1
                oneSeen = False

    if lista[0] == 1 and lista[-1] == 1:
        for i in range(len(lista)):
            if lista[i] == 1:
                oneSeen = True
            if lista[i] == 0 and oneSeen:
                kontor += 1
                oneSeen = False
        kontor+=1

    if lista[0]==0 and lista[-1] == 0:
        for i in range(len(lista)):
            if lista[i] == 0:
                oneSeen = True
            if lista[i] == 1 and oneSeen:
                kontor += 1
                oneSeen = False
    if lista[0]==1 and lista[-1] == 0:
        for i in range(len(lista)):
            if lista[i] == 1:
                oneSeen = True
            if lista[i] == 0 and oneSeen:
                kontor += 1
                oneSeen = False

    for i in lista:
        if i==1:
            kontor_1+=1
        elif i==0:
            kontor_0+=1
    if kontor_1==len(lista):
        kontor=1
    if kontor_0==len(lista):
        kontor=0

    return kontor



print(count_seq(list2))
