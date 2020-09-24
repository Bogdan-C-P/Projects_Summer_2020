x=int(input())
user_input_list=[]
for i in range(x):
    user_input_list.append(input().split(","))


output=[]
new_list=[]
for z in user_input_list:
    output = []
    for i in z:

        for j in range(len(i)):
            if i[j]=="(":
                output.append(i[j+1:])
            elif i[j]==")":
                for k in range(int(i[:j])):
                    output.append('0')
            elif "(" not in i and ")" not in i:
                output.append(i)
    new_list.append(output)

for i in new_list:
    print(','.join(i))