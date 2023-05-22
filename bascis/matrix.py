
r =int(input("Enter the number of rows"))
col=int(input("Enter the number of cols"))

a=list()
for i in range(r):
    b=list()
    for j in range(col):
        b.append(int(input(f"Enter the value for a[{i}][{j}]")))
    a.append(b)
for i in range(r):
    print(*a[i],end="\n")




print("Enetr the rows and coloumn for second matrix:\n")

r =int(input("Enter the number of rows"))
col=int(input("Enter the number of cols"))

a2=list()
for i in range(r):
    b=list()
    for j in range(col):
        b.append(int(input(f"Enter the value for a[{i}][{j}]")))
    a2.append(b)
for i in range(r):
    print(*a[i],end="\n")


print("-------------")

c=list()
for i in range(r):
    b=list()
    for j in range(col):
        ans=a[i][j]+a2[i][j]
        b.append(ans)
    c.append(b)
for i in range(r):
    print(*c[i],end="\n")
