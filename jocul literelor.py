p=[]
j=""
x=input()
for i in x:
    j+=i
for c in j.split():
    p.append(c)
alfa=p[0].lower()
beta=p[1].lower()
M=int(p[2])
N=int(p[3])
text=input().lower()
z, x, c = 0, 0, 0
list=text.lower().split()
for i in list:
    if i[0] == alfa.lower() and i[-1] == beta.lower():
        if len(i)<M:
            z+=1
        elif len(i)>=M and len(i)<N:
            x+=1
        elif len(i)>=N:
            c+=1
print(z, x, c)
