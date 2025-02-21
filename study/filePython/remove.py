import os 

if os.path.exists("study/filePython/name.txt"):
    os.remove("study/filePython/name.txt")
    print("Removed to sucess")
else: 
    print("The file does not exist")