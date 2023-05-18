import os
path="/Users/josephdevassy/Desktop/python/file.txt"

if os.path.exists(path):
    if os.path.isfile(path):
        print("is file")
    elif os.path.isdir(path):
        print("Directory")
    else:
        print("not file")
    
    print("exists")

else:
    print("not exists")

