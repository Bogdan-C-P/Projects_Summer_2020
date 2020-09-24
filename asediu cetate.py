x = input()
j=""
p=[]
for i in x:
    j+=i
for c in j.split(" "):
    p.append(c)
M=int(p[0])
N=int(p[1])
P=int(p[2])

lista_sold=[]
for v in range(N):
    lista_sold.append(v+1)

b=[]
for i in range(len(lista_sold)):
    b.append(lista_sold[(P-1+i) % len(lista_sold)])

while len(b)>1:
    poz=(M - 1) % len(b)
    b.remove(b[poz])
    c = []
    for j in range(len(b)):
        if poz== len(b):
            poz=0
        c.append(b[poz])
        poz+=1
    b = c


for i in b:
    print(i)




