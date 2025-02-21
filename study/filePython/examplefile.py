f = open("study/filePython/name.txt", "x")

f.write("My name is Pedro Henrique Araujo Cardoso")
f.close()

f = open("study/filePython/name.txt", "r")

print(f.read())

