try:
    file = pen('file.txt')
    str = f.readline()
    print(str)
except IOError:
    print("Error occured during Input...... Program Terminating....")
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error... Program Terminating...")
    