try:
    num = int(input("Enter the Number : "))
    print(num**2)
except (KeyboardInterrupt):
    print("You Should Have Entered a number... program Terminating...")
except (ValueError):
    print("Please check Before you enter... program Terminating...")
print("bye")