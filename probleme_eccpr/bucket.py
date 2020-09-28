x=int(input())
y=input()
sir=""
j=0

lista_numere=[]
for i in y.split():
    lista_numere.append(int(i))


dict={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,"12":0,"13":0,"14":0,"15":0,"16":0,"17":0,"18":0,"19":0}

for i in lista_numere:
    if i>=0 and i<10:
        dict["1"]+=1
    elif i>=10 and i<100:
        dict["2"]+=1
    elif i>=100 and i<1000:
        dict["3"]+=1
    elif i>=1000 and i<10000:
        dict["4"]+=1
    elif i>=10000 and i<100000:
        dict["5"]+=1
    elif i>=100000 and i<1000000:
        dict["6"]+=1
    elif i>=1000000 and i<10000000:
        dict["7"]+=1
    elif i>=10000000 and i<100000000:
        dict["8"]+=1
    elif i>=100000000 and i<1000000000:
        dict["9"]+=1
    elif i>=1000000000 and i<10000000000:
        dict["10"]+=1
    elif i>=10000000000 and i<100000000000:
        dict["11"]+=1
    elif i>=100000000000 and i<1000000000000:
        dict["12"]+=1
    elif i>=1000000000000 and i<10000000000000:
        dict["13"]+=1
    elif i>=10000000000000 and i<100000000000000:
        dict["14"]+=1
    elif i >= 100000000000000 and i < 1000000000000000:
        dict["15"] += 1
    elif i >= 1000000000000000 and i < 10000000000000000:
        dict["16"] += 1
    elif i >= 10000000000000000 and i < 100000000000000000:
        dict["17"] += 1
    elif i >= 100000000000000000 and i < 1000000000000000000:
        dict["18"] += 1
    elif i >= 1000000000000000000 and i < 10000000000000000000:
        dict["19"] += 1
for i in dict:
    if dict[i] >0:
        print(i, dict[i])