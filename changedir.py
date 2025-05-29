import os 
print("Current Working Directory is: ", os.getcwd())
os.chdir("New Dir")
print("After chdir, the current Directory is now......", end = ' ')
print(os.getcwd())