x=int(input())
user_input_list=[]
for i in range(x):
    user_input_list.append(input().split(","))
lista_rez=[]
output=[]
for i in range(len(user_input_list)):
    j=0
    output=[]
    lungime_lista=len(user_input_list[i])
    while j < lungime_lista:
        prepared_output = [user_input_list[i][j], 0]
        if user_input_list[i][j] != '0':
            kontor = 0
            j += 1
            while j < lungime_lista and user_input_list[i][j] == '0':
                kontor += 1
                j += 1
            prepared_output[1] = kontor
        if prepared_output[1] != 0:
            output.append('('+str(prepared_output[0])+','+str(prepared_output[1])+')')
        else:
            output.append(prepared_output[0])
    lista_rez.append(output)
for i in lista_rez:
    print(','.join(i))



