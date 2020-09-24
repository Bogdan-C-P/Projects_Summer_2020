def aranjamente(n,k):
    s1=1
    s2=1
    for i in range(1,n+1):
        s1*=i

    for j in range(1,n+1-k):
        s2*=j

    return s1/s2
x=input()
j=""
for i in x:
    j+=i
p=[]
for c in j.split():
    p.append(c)
k=int(p[0])
aranj=int(p[1])
n=[]
for elem in range(3600):
    n.append(elem+k)
list=[]
for i in n:
    if aranjamente(i,k)<=aranj:
        list.append(i)

if len(list)>=1:
    print(list[-1])
else:
    print("0")