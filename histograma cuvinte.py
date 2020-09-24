
propozitie=input()
prop1=""
for i in range(len(propozitie)):
    if propozitie[i] not in ["?",".","!"]:
        prop1+=propozitie[i].lower()
x=prop1.split()

d={}
for j in x:
    if j not in d:
        d[j]=1
    elif j in d:
        d[j]+=1

v=sorted(d.items(), key=lambda  x: x[0])
d1={}
for i in v:
    d1[i[0]]=i[1]

v1=sorted(d1.items(),key=lambda x:x[1],reverse=True)
for j in v1:
    print(j[0],j[1])
