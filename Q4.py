from utilities.math_operations import add, subtract
from utilities.string_operations import reverse_string, capitalize_string

def main():
    # Math operations
    print("Math Operations:")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Addition: ", add(num1, num2))
    print("Subtraction: ", subtract(num1, num2))
    
    # String operations
    print("\nString Operations:")
    input_string = input("Enter a string: ")
    print("Reverse String: ", reverse_string(input_string))
    print("Capitalize String: ", capitalize_string(input_string))

if __name__ == "__main__":
    main()