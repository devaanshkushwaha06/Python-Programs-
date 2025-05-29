import sys

# Print the current sys.path
print("Current sys.path:")
for path in sys.path:
    print(path)

# Explanation of module search
print("\nHow Python Searches for Modules:")
print("1. The directory of the script being executed.")
print("2. The directories listed in the PYTHONPATH environment variable (if set).")
print("3. Standard library directories.")
print("4. The site-packages directory for installed packages.")

# Adding a new directory to sys.path
new_directory = "D:/college pdf/semester 2/python/custom_modules"
sys.path.append(new_directory)  # Add the new directory to the module search path

print(f"\nAdded '{new_directory}' to sys.path.")
print("Updated sys.path:")
for path in sys.path:
    print(path)

# Importing a module from the newly added directory
try:
    import custom_module  # Replace 'custom_module' with the actual module name in the directory
    print("\nSuccessfully imported custom_module:")
    print("Custom Module Name:", custom_module.__name__)
except ImportError as e:
    print(f"Failed to import custom_module: {e}")