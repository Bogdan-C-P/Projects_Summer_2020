x = input()
y=""
for i in x:
    y+=i
lista=[]
for i in y.split():
    lista.append(i)

M=int(lista[0])
N=int(lista[1])
list_coduri=[]
z=""
for i in range(M):
    coduri=input()
    z+=coduri
    z+=" "
for k in z.split():
    list_coduri.append(k)

lista_produse=[]
produse=input()
y=""
for i in produse:
    y+=produse
    y+=" "
for i in y.split():
    lista_produse.append(i)
lista_produse2=[]
for i in range(N):
    lista_produse2.append(lista_produse[i])
print(list_coduri)
print(lista_produse2)
sum=0
for i in lista_produse2:
    for j in range(0,len(list_coduri),3):
        if i== list_coduri[j]:
            if list_coduri[j+1]=="p":
                sum+=float(list_coduri[j+2])


reduceri=0
for i in lista_produse2:
    for j in range(0,len(list_coduri),3):
        if i== list_coduri[j]:
            if list_coduri[j+1]=="c":
                reduceri+=float(list_coduri[j+2])
final_price=sum-sum*reduceri/100
print(round(final_price,2))
