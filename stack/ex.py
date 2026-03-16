s=[]

str="Anup"

for i in str:
    s.append(i)

print(s.pop())
print("top =", s[-1])


if(len(s)==0):
    print("stack is empty")

