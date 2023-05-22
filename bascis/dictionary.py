capitals={"kerela":"thiruva","tn":"chennai","karna":"benga"}

print(capitals["kerela"])
print(capitals.get("thiruva"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
print(capitals.get("kerela"))

capitals.update({"india":"delhi"})
capitals.pop("tn")


for keys,values in capitals.items():
    print(keys,values)


def hello1():
    print("hello world")
def hello(f,m,l):
    print("hello",f,m,l)
def hello2(*jk):
    for i in jk:
        print(i)



hello1()
hello(m="hai",f="hello",l="bei")
hello2("hai","hello","jjjj","kkkk")



a=10
b=20


print(f"hello {a} hai{b}")
print("hello {} hai {} ".format(a,b))
print("hello {1} hai {0} ".format(a,b))

print("hello{:.4f}".format(b))


import random
l=[1,2,3,4,5]

print(random.choice(l))

x=0
try:
    print("hello world")
    if x==0:
        raise Exception("value is zero")
except Exception as ae:
    print(ae)
except ZeroDivisionError as ae:
    print(ae)
except ArithmeticError as e:
    print(e)
finally:
    print("bei")


import os 


path="/Users/josephdevassy/Desktop/python/sample.py"


print(os.path.exists(path))
print(os.path.isfile(path))
print(os.path.isdir(path))





#os.replace("/Users/josephdevassy/Desktop/python/bascis/file2.txt","/Users/josephdevassy/Desktop/python/oop/file3")
#os.remove("/Users/josephdevassy/Desktop/python/oop/file3")

import typecasting


typecasting.hello()