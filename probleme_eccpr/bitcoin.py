x=input()
sir=""
for i in x:
    sir+=i
lista=[]
for j in sir.split():
    lista.append(j)
n=int(lista[0])
p=int(lista[1])

lista_zile=[]
lista_prognoze=[]

y=input()

for k in y.split():
    lista_zile.append(float(k))

for i in range(p):
    sum=0
    mean=0
    for j in lista_zile:
        sum+=j
    mean=sum/len(lista_zile)
    lista_prognoze.append(round(mean,2))
    lista_zile.append(round(mean,2))
    lista_zile.remove(lista_zile[0])
min=900
max=0
for i in lista_prognoze:
    if i>max:
        max=i
    if i<min:
        min=i

for i in lista_prognoze:
    print(i,end=" ")
print()
print(max,min)