#wrtielines function
file = open("file1.txt", "w")
lines = ["Hello world", "Welcome to the world of python", "Enjoy Learning Python"]
file.writelines(lines)
file.close()
print("Data written to file.......")