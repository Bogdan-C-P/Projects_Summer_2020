x=int(input())
lista_semnale=[]
for i in range(x):
    lista_semnale.append(input().split())

x=lista_semnale.copy()
new_list=[]
lista_finala=[]

def get_shifted_array(array,k):
    new_array=array.copy()
    for i in range(k):
        new_array.pop()
    for j in range(k):
        new_array.insert(0,0)
    return new_array

lungime=len(x)
for i in range(3):
    new_list=[]
    suma=0
    if i==0:
        for j in range(len(x)):
            x[j] = get_shifted_array(x[j], j*0)
        for j in range(10):
            suma = 0
            for k in range(lungime):
                suma += int(x[k][j])
            new_list.append(round(suma / lungime, 2))
    elif i==1:
        for j in range(len(x)):
            x[j]=get_shifted_array(x[j],j*1)
        for j in range(10):
            suma=0
            for k in range(lungime):
                suma+=int(x[k][j])
            new_list.append(round(suma/lungime,2))
    elif i == 2:
        for j in range(len(x)):
            x[j] = get_shifted_array(x[j], j )
        for j in range(10):
            suma = 0
            for k in range(lungime):
                suma += int(x[k][j])
            new_list.append(round(suma / lungime, 2))
    lista_finala.append(new_list)

new_list_intermediar=[]
new_lista_finala=[]

for i in lista_finala:
    new_list_intermediar=[]
    for j in i:
        new_list_intermediar.append("{:.2f}".format(j))
    new_lista_finala.append(new_list_intermediar)

for i in new_lista_finala:
    print(' '.join(i))