x=int(input())
vect1=[]
for i in range(x):
    y=int(input())
    vect1.append(y)
z=int(input())
vect2=[]
for j in range(z):
    c=int(input())
    vect2.append(c)

vect3=vect1+vect2
vect3.reverse()
dict={}
for k in vect3:
    dict[k]=0
    for m in vect3:

        if k>=m:
            dict[k]+=1


list=[]
for i in dict:
    if dict[i]>5:
        list.append(int(i))
mean=0
for i in list:
    mean+=i

print(round(mean/len(list),2))
