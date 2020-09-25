n=int(input())
m=int(input())

def prime(y):
    k=0
    for i in range(1,y):
        if y% i== 0:
            k+=1
    return k



matrix=[]
for i in range(n):
    for j in range(m):
        x=int(input())
        matrix.append(x)

matrix2=[]
for i in matrix:
    if prime(i)==1:
        matrix2.append(0)
    else:
        matrix2.append(1)
sum=0
for i in matrix2:
    sum+=i

print(sum)




