def combinari(n,k):
    s1=1
    s2=1
    s3=1
    for i in range(1,n+1):
        s1*=i
    for j in range(1,k+1):
        s2*=j
    for k in range(1,n-k+1):
        s3*=k
    return s1/(s2*s3)

x=input()
y=""
z=[]
for i in x:
    y+=i
for j in y.split():
    z.append(j)

n=int(z[0])
M=int(z[1])
print(n,M)
lista_k=[]
lista_rezolvare=[]
for i in range(n):
    lista_k.append(i)

for j in lista_k:
    if combinari(n, j) >= M:
        lista_rezolvare.append(j)

if len(lista_rezolvare)>=1:
    print(lista_rezolvare[0])
else:
    print(0)
