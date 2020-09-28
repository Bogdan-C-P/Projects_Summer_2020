x= int(input())
sir=""
lista_nr=[]
for i in range(x):
    y=input()
    sir+=y
    sir+=" "

for i in sir.split():
    lista_nr.append(int(i))

def transf_binar(x):
    lista_binar=[]
    while x>0:
        c=x%2
        x=int(x/2)
        lista_binar.append(c)
    while len(lista_binar)<8:
        lista_binar.insert(0,0)
    return lista_binar


lista_noua=[]
for i in lista_nr:
    lista_noua.append(transf_binar(i))

contor=0
lista_contor=[]
for i in lista_noua:
    for j in i:
        if j==0:
            contor+=1
    lista_contor.append(contor)
    contor=0
max=0
for i in range(len(lista_contor)):
    if lista_contor[i]>max:
        max=lista_contor[i]
for i in range(len(lista_contor)):
    if lista_contor[i]==max:
        print(lista_nr[i])



