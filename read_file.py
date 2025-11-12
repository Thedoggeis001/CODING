import os
import sys

def read_and_print_file():
    """
    Asks the user for the name of a file, searches for it in the program's directory,
    opens it, and prints its contents.
    """
    print("--- TEXT FILE READER ---")
    
    # 1. Get the directory path of the running program
    # *Fix: Get the absolute path of the currently running .py file
    if getattr(sys, 'frozen', False):
        # If the executable was 'frozen' (e.g., with PyInstaller)
        program_dir = os.path.dirname(sys.executable)
    else:
        # Normal path of the Python file
        program_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Ask the user for the name of the file to read
    requested_filename = input("Enter the name of the text file (e.g., myfile.txt): ")

    # 2. Build the full file path
    # *Fix: Join the program directory with the filename
    full_path = os.path.join(program_dir, requested_filename)
    
    print(f"Looking for the file at: {full_path}")

    try:
        # Try to open the file using the full path
        # *Fix: Use the 'full_path' variable
        with open(full_path, 'r', encoding='utf-8') as file:
            # Read the entire content of the file
            content = file.read()
            
            print(f"\n--- Content of '{requested_filename}' ---\n")
            print(content)
            print("\n------------------------------------")
            
    except FileNotFoundError:
        # Handle the error if the file is not found
        print(f"\n*ERROR: The file '{requested_filename}' was not found in the program directory.")
        print(f"Program directory: {program_dir}")
        
    except Exception as e:
        # Handle any other errors
        print(f"\n*GENERAL ERROR while reading the file: {e}")

# Run the function
read_and_print_file()
