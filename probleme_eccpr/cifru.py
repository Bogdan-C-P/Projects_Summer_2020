text=input()
y=""
for i in text:
    y+=i

criptare1=input()
x=""
for i in criptare1:
    x+=i
criptare=[]
for j in x.split():
    criptare.append(j)
dict={}
for i in criptare:
    dict[i[0]]=i[2]

new_text=""
'''
for i in y:
   if i not in ".!(){}[]?/\|;:,'_-' ":
        new_text+=dict[i]
   else:
       new_text+=i
'''
for i in y:
    if i in dict:
        new_text+=dict[i]
    else:
        new_text+=i
print(new_text)
