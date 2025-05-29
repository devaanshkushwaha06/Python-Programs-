import os
import sys

# Function to list all installed packages
def list_installed_packages():
    print("Installed Python Packages:")
    installed_packages = sorted(sys.modules.keys())
    for package in installed_packages:
        print(package)

# Function to check if a specific package is installed
def check_package(package_name):
    try:
        __import__(package_name)
        print(f"\nThe package '{package_name}' is installed.")
    except ImportError:
        print(f"\nThe package '{package_name}' is NOT installed.")

# List all installed packages
list_installed_packages()

# Check if 'numpy' is installed
check_package('numpy')