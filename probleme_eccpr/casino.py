x = int(input())
lista=[]
sir=""
for i in range(x):
    y=input()
    sir+=y
    sir+=" "

for j in sir.split():
    try:
        lista.append(int(j))
    except:
        lista.append((j))

dict_trefla={}
dict_caro={}
dict_pica={}
dict_cupa={}
list_trefla=[]
list_cupa=[]
list_caro=[]
list_pica=[]
for i in range(1,len(lista),2):
    if lista[i]=="caro":
        if lista[i-1] not in dict_caro:
            dict_caro[lista[i-1]]=1
        else:
            dict_caro[lista[i-1]]+=1
        if dict_caro[lista[i-1]]>2:
            list_caro.append(lista[i-1])
    elif lista[i]=="trefla":
        if lista[i-1] not in dict_trefla:
            dict_trefla[lista[i-1]]=1
        else:
            dict_trefla[lista[i-1]]+=1
        if dict_trefla[lista[i-1]]>2:
            list_trefla.append(lista[i-1])
    elif lista[i]=="cupa":
        if lista[i-1] not in dict_cupa:
            dict_cupa[lista[i-1]]=1
        else:
            dict_cupa[lista[i-1]]+=1
        if dict_cupa[lista[i-1]]>2:
            list_cupa.append(lista[i-1])
    elif lista[i]=="pica":
        if lista[i-1] not in dict_pica:
            dict_pica[lista[i-1]]=1
        else:
            dict_pica[lista[i-1]]+=1
        if dict_pica[lista[i-1]]>2:
            list_pica.append(lista[i-1])
onseen=True
if onseen == True:
    for i in dict_pica:
        if dict_pica[i]>2:
            print(list_pica[0], "pica")
            onseen = False
            break
if onseen==True:
    for i in dict_caro:
        if dict_caro[i]>2:
            print(list_caro[0], "caro")
            onseen=False
            break
if onseen == True:
    for i in dict_trefla:
        if dict_trefla[i]>2:
            print(list_trefla[0], "trefla")
            onseen=False
            break
if onseen == True:
    for i in dict_cupa:
        if dict_cupa[i]>2:
            print(list_cupa[0], "cupa")
            onseen = False
            break


if onseen==True:
    print("JOC OK")


