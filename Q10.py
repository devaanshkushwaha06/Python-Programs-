import importlib

# Ask the user for the module name
module_name = input("Enter the module name to import: ")

try:
    # Dynamically import the module
    module = importlib.import_module(module_name)
    print(f"Module '{module_name}' imported successfully.")

    # List all callable functions in the module
    functions = [func for func in dir(module) if callable(getattr(module, func))]
    print("\nAvailable functions in the module:")
    print(", ".join(functions))

    # Ask the user for the function name
    function_name = input("Enter the function name to call: ")

    if function_name in functions:
        # Get the function dynamically
        func = getattr(module, function_name)

        # Call the function (you can modify this to accept arguments dynamically)
        result = func()  # For simplicity, assuming the function takes no arguments
        print(f"Result of calling '{function_name}': {result}")
    else:
        print(f"Function '{function_name}' does not exist in module '{module_name}'.")
except ImportError:
    print(f"Module '{module_name}' could not be imported.")
except Exception as e:
    print(f"An error occurred: {e}")