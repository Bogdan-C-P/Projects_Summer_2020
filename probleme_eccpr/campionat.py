k=int(input())
n=int(input())
list1=[]
string1=""
for i in range(n):
    y=input()
    string1+=y
    string1+=" "

string2=""
for i in string1:
    if i!="-":
        string2+=i

list1=[]
for i in string2.split():
    list1.append(i)
list2=[]

for i in list1:
    try:
        list2.append(int(i))
    except:
        list2.append(i)

list_exchipe=[]
list_scor=[]
for i in list2:
    if type(i)==str:
        list_exchipe.append(i)
    elif type(i)==int:
        list_scor.append(i)
lista_finala=[]
for i in range(len(list_scor)):
    lista_finala.append(list_exchipe[i])
    lista_finala.append(list_scor[i])

dict1={}
dict2={}
dict3={}
for i in lista_finala:
    if type(i)==str:
        dict1[i]=0
        dict2[i] = 0
        dict3[i] = 0

for i in range(0,len(lista_finala)-3,4):
    if lista_finala[i] in dict1:
        if lista_finala[i+1]>lista_finala[i+3]:
            dict1[lista_finala[i]]+=3
        elif lista_finala[i+1]<lista_finala[i+3]:
            dict1[lista_finala[i+2]]+=3
        elif  lista_finala[i+1]==lista_finala[i+3]:
            dict1[lista_finala[i]] += 1
            dict1[lista_finala[i+2]] += 1

for i in range(0,len(lista_finala)-1,2):
    if lista_finala[i] in dict2:
        dict2[lista_finala[i]]+=lista_finala[i+1]

for i in range(0,len(lista_finala)-1,4):
    if lista_finala[i] in dict3:
        dict3[lista_finala[i]]+=lista_finala[i+3]
        dict3[lista_finala[i+2]]+=lista_finala[i+1]

d1={}
d1=sorted(dict1.items() , key = lambda x:x[1],reverse=True)
d2={}
for i in d1:
    d2[i[0]]=i[1]
for key in d2:
    print(key,dict1[key],dict2[key],dict3[key])

