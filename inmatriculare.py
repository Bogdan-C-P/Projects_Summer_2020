def type_sub(a):
    list3 = []
    list4 = []
    for i in a:
        list3.append(i)
    for j in list3:
        try:
            j = int(j)
        except:
            j = j
        list4.append(j)
    kontor = 0
    for i in list4:
        if (type(i)) == int:
            kontor += 1
    if len(a)==kontor:
        return True
    else:
        return False

def type_third(b):
    list3 = []
    list4 = []
    for i in b:
        list3.append(i)
    for j in list3:
        try:
            j = int(j)
        except:
            j = j
        list4.append(j)
    kontor = 0
    for i in list4:
        if (type(i)) == str:
            kontor += 1
    if len(b)==kontor:
        return True
    else:
        return False


inputs=[]
while True:
    x=input()
    if x== "":
        break
    inputs.append(x)
    inputs.append(" ")

inputs2=[]
for i in inputs:
    for j in i:
        inputs2.append(j)
y=""
for i in inputs2:
    y+=i
list=[]
for j in y.split():
    list.append(j)

list1=[]
string1="AB,AR,AG,B,BC,BH,BN,BT,BV,BR,BZ,CS,CL,CJ,CT,CV,DB,DJ,GL,GR,GJ,HR,HD,IL,IS,IF,MM,MH,MS,NT,OT,PH,SM,SJ,SB,SV,TR,TM,TL,VS,VL,VN"
for k in string1.split(","):
    list1.append(k)

for i in range(0,len(list),3):
    str2 = ""
    for k in list[i+2]:
        str2 += k
    if list[i] in list1 and len(list[i+1])>1 and len(list[i+1])<4 and type_sub(list[i+1])==True and len(list[i+2])>2 and len(list[i+2])<4 and str2.isupper()==True and type_third(list[i+2])==True:
        print(list[i], list[i+1], list[i+2])