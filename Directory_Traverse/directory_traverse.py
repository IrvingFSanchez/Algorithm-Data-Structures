#Name: Irving F. Sanchez
#Course: Algorithm and Data Structures SP25-CPSC-34000-002
#School: Lewis University, Romeoville, IL
#Purpose: Design a pthon program that traverses a directory and prints out the files and directories within it ensuring proper indentation

'''Note: I put a ton of comments in my code for personal use, I add notes to help me understand what
I'm doing and why I'm doing it.I'm not sure if this is a good practice or not, but I'm doing it for now.'''

import os

''' /*---+---+---+--Start of Traversal Function Block---+---+---+--*/ '''

class ErrorManager:
    
    # This block ensures that permission errors and invalid paths are caught and handled without crashing the program
    
    def __enter__(self):
        # This method will be called when entering the 'with' block
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        # This method will be called when exiting the 'with' block and specifically handles particular errors
        if exc_type == PermissionError:
            print("[Permission Denied] You do not have permission to access this directory.")
            return True # This will suppress the error
        elif exc_type == FileNotFoundError:
            print("[Invalid Path] The path you entered does not exist.")
            return True
        return False
''' /*---+---+---+--End of Traversal Function Block---+---+---+--*/ '''



''' /*---+---+---+--Start of Directory Traversal Generator Block---+---+---+--*/ '''

def traverse_directory(via, gradus=0):
    # This block will traverse the directory and print out the files and directories within it ensuring indentation
    
    with ErrorManager():
        # Here we list all items in the current directory
        for index, res in enumerate(os.listdir(via)): # res means item in latin
            # Here we create the full path for the current item
            iter_path = os.path.join(via, res)
            
            # Here we check to see if this is the last item in the directory for proper tree formatting
            is_last = index == len(os.listdir(via)) - 1
            
            # Here we format the output with a tree-like structure for better readability
            prefix = "    " * (gradus - 1) + ("└── " if is_last else "├── ") # Just a creative way to create the tree structure
            yield prefix + res
            
            if os.path.isdir(iter_path):
                # If the item is a directory, recursively traverse it
                yield from traverse_directory(iter_path, gradus + 1)
                
''' /*---+---+---+--End of Directory Traversal Generator Block---+---+---+--*/ '''



''' /*---+---+---+--Start of Main Function Block---+---+---+--*/ '''

def main():
    
    while True:
        # This block will handle user input and initiates the directory traversal for this program
        via = input("\nPlease enter the directory you want to traverse: ")
        
        # Here we check to see if the path is valid and or exists
        if os.path.exists(via):
            print(via) # This will print the root directory
            # This will traverse the directory and print each item
            for line in traverse_directory(via, 1):
                print(line)
        else:
            print("[Invalid Path] The path you entered does not exist. Please try again.")
            
        continuare = input("\nWould you like to traverse another directory? (yes/no): ").strip().lower()
        if continuare not in ('yes', 'y'):
            print("Exiting program...\n")
            break

''' /*---+---+---+--End of Main Function Block---+---+---+--*/ '''



''' /*---+---+---+--Start of Program Execution Block---+---+---+--*/ '''

if __name__ == "__main__":
    # This block ensures the main function is called only 
    main()
    
''' /*---+---+---+--End of Program Execution Block---+---+---+--*/ '''