a=1
b='e'
c='ere'
d="string"
e=7.5
print(type(a),type(b),type(c),type(d),type(e))
print(a,b)
a+=1
print(a)

print(str(a)+b+c+d+str(e))


a,b,c,d,e=1,2,3,4,"rtr"
a=b=c=d=e=45

str="hello world"
print(len(str))
print(str.count('o'))
print(str.find('e'))
print(str.endswith('l'),str.isalnum(),str.index('e'),str.islower(),str.isupper(),str.replace('o','w'),str.lstrip())

a=18

if a>10 and a <15:
    print(a)
elif a>5 or a<9:
    print(a-1)
else:
    print(a-2)


i="t"

#while len(i)!=0:
 #  print("continue")

for i in range(1,101):
    print(i)
for i in "bro code":
    print(i)
import time

for i in range(10,-1,-1):
    #time.sleep(1)
    print(i)


for i in range(5,-1,-1):
    for j in range(i,5):
        print("*",end=" ")
    print()
for i in range(5):
    if i==5:
        break
   
    if i==3:
        continue
    
    if i==1:
        pass
    print(i)
