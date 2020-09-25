x=int(input())

def medie_geom(x,y):
    return round(x**(1/y),2)
sir=""
lista_mancare=[]
for i in range(x):
    y=input()
    sir+=y
    sir+=" "

for i in sir.split():
    try:
        lista_mancare.append(int(i))
    except:
        lista_mancare.append((i))

sir2=""
while True:
    try:
        y = input()
    except EOFError:
        break
    sir2 += y
    sir2 += " "
    if y=="":
        break
lista_emotii=[]
for i in sir2.split():
    lista_emotii.append(i)

dict={}
for i in range(2,len(lista_emotii),3):
    dict[lista_emotii[i]]=1
dict_emotii={}
for i in range(2,len(lista_emotii),3):
    if lista_emotii[i] in dict_emotii:
        dict_emotii[lista_emotii[i]]+=1
    else:
        dict_emotii[lista_emotii[i]]=1

for i in range(len(lista_emotii)):
    for j in range(len(lista_mancare)):
        if lista_emotii[i] == lista_mancare[j]:
            dict[lista_emotii[i+1]]*=lista_mancare[j+1]

for i in dict:
    if dict_emotii[i]>1:
        dict[i]=medie_geom(dict[i],dict_emotii[i])

z=sorted(dict.items(), key=lambda x:x[1],reverse=True)

for i in z:
    print(i[0],"{:.2f}".format(i[1]))
