file = open("./text.txt")

for line in file :
    print(line)

file.seek(0)


file.close()