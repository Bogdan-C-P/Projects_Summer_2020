x=int(input())

lista_elem=[]
for i in range(x):
    lista_elem.append(int(input()))

lista_sume=[]
lista_kontor=[]
print(lista_elem)
for j in range(len(lista_elem)):
    lista_copie=lista_elem
    suma = 0
    kontor=0
    for k in lista_copie:
        suma+=k
        kontor+=1
        if suma%3==0:
            lista_sume.append(suma)
            lista_kontor.append(kontor)
    lista_elem.remove(lista_elem[0])

print(lista_sume)
print(lista_kontor)
max=0
max2=0
lista_sume2=[]
for i in lista_kontor:
    if i >max:
        max=i

for i in range(len(lista_kontor)):
    if lista_kontor[i] == max:
        lista_sume2.append(lista_sume[i])

for i in lista_sume2:
    if i>max2:
        max2=i


if len(lista_sume)==0 or lista_sume[0]==0:
    print(0)
elif len(lista_sume)>0:

        print(max, max2)


