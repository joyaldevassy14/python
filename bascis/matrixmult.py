r1=int(input("Enter the number of rows for matrix1 "))
c1=int(input("Enter the number of cols for matrix2 "))

a1=list()
for i in range(r1):
    b=list()
    for j in range(c1):
        b.append(int(input(f"Enetr the value for a1[{i}][{j}] ")))
    a1.append(b)
print("Enetred matrix is :\n")
for i in range(r1):
    print(*a1[i],end="\n")


r2=int(input("Enter the number of rows in matrix1 "))
c2=int(input("Enter the number of cols in matrix2 "))

a2=list()
for i in range(r2):
    b=list()
    for j in range(c2):
        b.append(int(input(f"Enter the value for a2[{i}][{j}] ")))
    a2.append(b)
print("Entered matrix is:\n")

for i in range(r2):
    print(*a2[i])


a3=list()
for i in range(r2):
    b=list()
    for j in range(c2):
        b.append(a1[i][j]*a2[i][j])
    a3.append(b)

print("the resultant matrix is :\n")


for i in range(r2):
    print(*a3[i],end="\n")