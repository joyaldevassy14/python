l=list()

for i in range(1):
    l.append(input("enter the number"))
print(*l)

for x in l:
    print(x)

l[0]="hello"
print(l)

l.pop()
l.insert(3,"hai")
l.sort()
l.clear()
print(l)


l1=["hai","hlo"]
l2=["a","b","c"]
l3=["ab","cd","de"]
l4=[l1,l2,l3]
print(l4[2][1])

z=10
x=11

print(f"the value is {z} and {x}")


z=[]
y=["hlo","hi"]
x=["vvv","ffff"]
z.append(y)
z.append(x)
print(*(z))


