#with open("file1.txt", "rb") as file:
#    for line in file:
#        print(line)
#print("Let's Check if the file is closed : ", file.close())

#second example

file= open("file1.txt", "rb")
for line in file:
    print(line)
print("Let's Check if the file is closed : ", file.close())