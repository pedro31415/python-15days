# f = open("study/filePython/arquivo.txt", "r")

# # read lines in file
# print(f.read())
# print(f.readline())
# f.close()

f = open("study/filePython/arquivo.txt", "w")

f.write("Now the file has more content")
f.close()

f = open("study/filePython/arquivo.txt", "a")
f.write("The game of thrones is the best serie forever")
f.close()

f = open("study/filePython/arquivo.txt", "r")

print(f.read())