try:
    file = open('file.txt')
    str = file.readline()
    print(str)
except IOError:
    print("Error occured during Input.... Program Terminating....")
else:
    print("Program Terminating Succesfully...")

print("-------------------------------------------second example---------------------------------------------")

#second Example

try:
    file = open('file.txt')
    str = f.readline()
    print(str)
except:
    print("Error occurred .... Program Terminated....")
else:
    print("Program Terminating Successfully...")
    