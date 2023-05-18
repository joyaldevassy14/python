import os 


src="file2.txt"
dest="/Users/josephdevassy/Desktop/Web Development/file3.txt" #location path with filename 


try:
    if os.path.exists(dest):
        print("file already exits")
    else:
        os.replace(src,dest)


except FileNotFoundError:
    print("file not found")



#deleting a file

os.remove('file2.txt')