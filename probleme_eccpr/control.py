
x=int(input())
def get_lungime(x,y,w,z):
    return ((z-y)**2+(w-x)**2)**(1/2)
sir=""
for i in range(x):
    y=input()
    sir+=y
    sir+=" "
lista_nr=[]
for i in sir.split():
    lista_nr.append(float(i))
onseen=False
if len(lista_nr)/2==3:
    if get_lungime(lista_nr[0],lista_nr[1],lista_nr[2],lista_nr[3]) == get_lungime(lista_nr[2],lista_nr[3],lista_nr[4],lista_nr[5]) and get_lungime(lista_nr[0],lista_nr[1],lista_nr[2],lista_nr[3])==get_lungime(lista_nr[4],lista_nr[5],lista_nr[0],lista_nr[1]):
        onseen=True

if len(lista_nr)/2>3:
    for i in range(0,len(lista_nr)-5,2):
        if abs(1-get_lungime(lista_nr[i],lista_nr[i+1],lista_nr[i+2],lista_nr[i+3])/get_lungime(lista_nr[i+2],lista_nr[i+3],lista_nr[i+4],lista_nr[i+5]))<=0.0001 and abs(1-get_lungime(lista_nr[0],lista_nr[1],lista_nr[2],lista_nr[3])/get_lungime(lista_nr[-1],lista_nr[-2],lista_nr[0],lista_nr[1]))<=0.0001:
            onseen=True

if onseen==True:
    print("da")
else:
    print("nu")