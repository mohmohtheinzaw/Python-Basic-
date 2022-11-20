file = open("./text.txt")

# for line in file :
#     print(line)

# file.seek(0)
linelist = file.readlines()
print(linelist)

file.close()

with open('./text.txt') as file :
    for line in file :
        print(line) ;
print('other work')