a=int(input("Enter the number 1 \t"))
b=int(input("Enter the number 2\t"))

try:
    c=a/b
    
except ZeroDivisionError as e:
    print(e)
    print("Divisoin by zero not possible")
except ArithmeticError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(c)
finally:
    print("final block")
