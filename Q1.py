# script.py

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
