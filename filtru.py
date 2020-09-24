x=input()
text=""
for j in x:
    text+=j

nr=int(input())
cuv_cenzura1=[]
cuv_cenzura=[]
cuv=""
y=input()

for j in y:
    cuv+=j
for i in cuv.split():
    cuv_cenzura1.append(i)
for k in range(nr):
    cuv_cenzura.append(cuv_cenzura1[k]) 


for i in cuv_cenzura:
    text=text.replace(i,"*"*len(i))


print(text)

