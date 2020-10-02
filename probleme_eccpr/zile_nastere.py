n=int(input())
lista_zile=[]
sir=""
for i in range(n):
    sir+=input()
    sir+=" "

sir2=""
j=0
for i in sir:
    j+=1
    if j%3!=0:
        sir2+=i

sir3=""
k=0
for i in range(len(sir2)):
    k+=1
    if k%2==0:
        sir3+=sir2[i]
        sir3+=" "
    else:
        sir3+=sir2[i]

lista_zile_2=[]
for i in range(0,len(sir3.split()),2):
    lista_zile_2.append(tuple(sir3.split()[i:i+2]))

lista_zile_3=[]
dictionar={}
for i in lista_zile_2:
    if j in dictionar:
        dictionar[i] += 1
    else:
        dictionar[i] = 1

for i in dictionar:
    lista_zile_3.append(i)


z=sorted(lista_zile_3, key=lambda x: (x[1],x[0]))

for i in z:
    c=0
    for v in range(len(i)):
        c+=1

        if c==1:
            print(i[v], end="")
            print("-",end="")
        else:
            print(i[v],end="")
    print()
