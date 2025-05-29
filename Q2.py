'''import math_operations'''
# Import the custom module
import math_operations

# Example inputs
num1 = float(input("Enter the First Number: "))
num2 = float(input("Enter the Second Number: "))

# Call the functions and print results
print(f"Addition of {num1} and {num2}: {math_operations.add(num1, num2)}")
print(f"Subtraction of {num1} and {num2}: {math_operations.subtract(num1, num2)}")
print(f"Multiplication of {num1} and {num2}: {math_operations.multiply(num1, num2)}")
print(f"Division of {num1} by {num2}: {math_operations.divide(num1, num2)}")

print("---------------------------------------------------------")


'''from math_operations import add, subtract'''
print("Printing the math operation by calling specific fucntion")

# Import specific functions from the module
from math_operations import add, subtract

# Example inputs
num1 = float(input("Enter the First Number: "))
num2 = float(input("Enter the Second Number: "))

# Call the imported functions directly
print(f"Addition of {num1} and {num2}: {add(num1, num2)}")
print(f"Subtraction of {num1} and {num2}: {subtract(num1, num2)}")

# Note: For multiply and divide, you'd need to import them or use another import style.

print("---------------------------------------------------------")
'''from math_operations import *'''
print("importing all functions together")

# Import all functions from the module
from math_operations import *

# Example inputs
num1 = float(input("Enter the First Number: "))
num2 = float(input("Enter the Second Number: "))

# Call all the functions directly
print(f"Addition of {num1} and {num2}: {add(num1, num2)}")
print(f"Subtraction of {num1} and {num2}: {subtract(num1, num2)}")
print(f"Multiplication of {num1} and {num2}: {multiply(num1, num2)}")
print(f"Division of {num1} by {num2}: {divide(num1, num2)}")
