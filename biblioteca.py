lista_dimens=[]
lista_dimens.append(input().split())
D=int(lista_dimens[0][0])
k=int(lista_dimens[0][1])
sir=""
lista_carti=[]

for i in range(k):
    y=input()
    sir+=y
    sir+=" "
for j in sir.split():
    lista_carti.append(int(j))

new_list=[]
for i in range(0,len(lista_carti),2):
    for j in range(lista_carti[i]):
        new_list.append(lista_carti[i+1])

new_list2 = sorted(new_list, reverse=True)

i = 0
while len(new_list2) > 0:
    copy = D
    i = 0
    while i < len(new_list2):
        if copy >= new_list2[i]:
            copy -= new_list2[i]
            print(new_list2[i], end=" ")
            new_list2.remove(new_list2[i])

        else:
            i += 1
    print()