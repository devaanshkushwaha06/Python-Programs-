# math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed"

# Define a main function for testing
def main():
    print("Testing math_operations module:")
    print(f"Addition: {add(10, 5)}")
    print(f"Subtraction: {subtract(10, 5)}")
    print(f"Multiplication: {multiply(10, 5)}")
    print(f"Division: {divide(10, 5)}")
    print(f"Division by zero: {divide(10, 0)}")

# Use the __name__ construct to ensure main() runs only when executed directly
if __name__ == "__main__":
    main()