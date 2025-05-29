# Import the entire module
import utilities.math_operations

# Access functions using the module name
print(f"Addition: {utilities.math_operations.add(10, 5)}")
print(f"Subtraction: {utilities.math_operations.subtract(10, 5)}")
print(f"Multiplication: {utilities.math_operations.multiply(10, 5)}")
print(f"Division: {utilities.math_operations.divide(10, 5)}")
print("----------------------------------------------------------------------------")

# Import the module directly
from utilities import math_operations

# Access functions using the module name
print(f"Addition: {math_operations.add(10, 5)}")
print(f"Subtraction: {math_operations.subtract(10, 5)}")
print(f"Multiplication: {math_operations.multiply(10, 5)}")
print(f"Division: {math_operations.divide(10, 5)}")

print("--------------------------------------------------------------------------")

# Import specific function directly
from utilities.math_operations import add

# Access the imported function directly
print(f"Addition: {add(10, 5)}")

# Attempting to access other functions will cause an error
# print(math_operations.subtract(10, 5))  # This will raise a NameError