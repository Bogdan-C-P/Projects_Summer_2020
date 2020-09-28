x=input()

dictionar={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22, "W":23,"X":24,"Y":25,"Z":26}
lista_caractere=[]
sir=""
i=0

while i<len(x)-1:
    if int(x[i])*10+int(x[i+1])>26:
        lista_caractere.append(int(x[i]))
    elif int(x[i])==0 and int(x[i+1])==0:
        lista_caractere.append(" ")
        i+=1
    elif int(x[i])==0 and int(x[i+1])!=0:
        lista_caractere.append(int(x[i+1]))
        i+=1
    elif int(x[i])*10+int(x[i+1])<=26:
        lista_caractere.append(int(x[i])*10+int(x[i+1]))
        i+=1
    elif i==len(x)-3 and int(x[i])*10+int(x[i+1])<26 :
        lista_caractere.append(int(x[i+2]))
    i+=1



for j in lista_caractere:
    if j == " ":
        sir+=" "
    for k in dictionar:
        if dictionar[k]==j:
            sir+=k



print(sir)

