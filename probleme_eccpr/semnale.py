x=int(input())
semnal=[]
for i in range(x):
    y=float(input())
    semnal.append(y)

list1=[]
for i in range(len(semnal)):
    if i==0:
        if semnal[i]>semnal[i+1]:
            list1.append(semnal[i])
    elif i>0 and i<len(semnal)-1:
        if semnal[i]>semnal[i-1] and semnal[i]>semnal[i+1]:
            list1.append(semnal[i])
    else :
        if semnal[i]>semnal[i-1]:
            list1.append(semnal[i])

sum=0
for i in list1:
    sum+=i
mean=sum/len(list1)
kontor=0
for i in semnal:
    if i>mean:
        kontor+=1

print(kontor)
