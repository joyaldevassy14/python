try:
    with open("file.txt") as file:
        print(file.read())
    print(file.closed)
except FileNotFoundError as e :
    print(e)
    print("file not found ")