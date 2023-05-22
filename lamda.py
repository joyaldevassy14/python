double=lambda x:x*2
double2=lambda x,y:x+y
double3=lambda:print("hello")

print(double(5))
print(double2(4,5))
print(double3())


l=["1","0","2","3","7","4"]
l2=sorted(l,reverse=True)

l.sort(reverse=True)
l2=l
print(*l2)


store=[("1",40),("2",3)]


to_euro=lambda data:(data[0],data[1]*2)



l5=list(map(to_euro,store))

print(l5)