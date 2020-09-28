x=int(input())
lista_aruncari = []
for i in range(x):
    lista_aruncari.append(int(input()))

dict_aruncari = {}
for j in lista_aruncari:
    if j not in dict_aruncari:
        dict_aruncari[j]=1
    elif j in dict_aruncari:
        dict_aruncari[j]+=1

print(lista_aruncari)

d2=sorted(dict_aruncari.items(), key=lambda x:x[1])
if len(d2)>1:
    dif=d2[-1][1]-d2[0][1]
else:
    dif=d2[-1][1]-1
procent=x/10

if dif>procent:
    print(1)
else:
    print(0)