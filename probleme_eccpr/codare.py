x= int(input())
sir=""
lista_nr=[]
for i in range(x):
    y=input()
    sir+=y
    sir+=":"
sir2=""
for i in sir:
    if i!=" ":
        sir2+=i
for i in sir2.split(":"):
    lista_nr.append(i)

lista_nr.remove("")

def prima_transf(x):
    sir2=""

    for i in range(0,len(x)-1,2):
        sir2+=x[i+1]
        sir2+=x[i]
    if len(x) % 2 == 1:
        sir2+=x[-1]
    return sir2

def second_transf(x):
    lista=[]
    lista.append(int(x[0]))
    for i in range(1,len(x)):
        lista.append(int(x[i])%2)
    return lista
lista3=[]
for i in lista_nr:
    lista3.append(prima_transf(i))

lista4=[]
for i in lista3:
    lista4.append((second_transf(i)))

max=0
lista_sume=[]
for i in lista4:
    suma=0
    for j in i:
        suma+=j
    lista_sume.append(suma)
for i in lista_sume:
    if i>max:
        max=i
for i in range(len(lista_sume)):
    if lista_sume[i]==max:
        print(lista_sume[i])
        break