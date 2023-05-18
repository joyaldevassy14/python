try:
    text="hello world i write this text"
    with open('file.txt','w') as file:   # w for overwriting 
        file.write(text)
        print("file overwritten")
    with open('file.txt','a')as file:   #a for appending text
        file.write(text)
        print("append text")
    with open('file.txt','r') as file:   #r for reading 
         print(file.read())
except FileNotFoundError as e:
    print(e)
    print("error")