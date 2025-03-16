# Name: Irving F. Sanchez
# Course: Algorithm and Data Structures SP25-CPSC-34000-002
# School: Lewis University, Romeoville, IL
# Purpose: Design school_locker program to mimic low-level memory management, similar to how languages like C handle arrays

'''Note: I put a ton of comments in my code for personal use, I add notes to help me understand what
I'm doing and why I'm doing it. I'm not sure if this is a good practice or not, but I'm doing it for now.'''

import ctypes

''' /*---+---+---+--Start of Locker Class Block---+---+---+--*/ '''

class SchoolLockerSystem:
    
    ### INITIALIZE LOCKER SYSTEM ###
    def __init__(self, initial_lockers=1):
        # This just provides initial values for the locker system
        self.capacity = initial_lockers  # This is the total number of lockers in the system
        self.num_lockers = 0  # This is the number of lockers currently in use
        self.lockers = self._make_array(self.capacity)  # This is the array that will hold the lockers (allocate raw memory for lockers)
    
    ### Allocate Memory for Lockers ###
    def _make_array(self, capacity):
        # This allocates raw memory for the lockers using ctypes
        return (capacity * ctypes.py_object)()
    
    ### ADD LOCKERS FUNCTION ###
    def add_locker(self, item):
        if self.num_lockers == self.capacity:
            self._expand_lockers()  # If we run out of lockers, we need to expand the system to add more lockers
        self.lockers[self.num_lockers] = item
        self.num_lockers += 1
        print(f"Added locker {item} to the system at position {self.num_lockers - 1}")
    
    ### INSERT LOCKER FUNCTION ###
    def insert_locker(self, index, item):
        if index < 0 or index > self.num_lockers:
            print("Error: Invalid locker position!")
            return
        if self.num_lockers == self.capacity:
            self._expand_lockers()
        for i in range(self.num_lockers, index, -1):
            self.lockers[i] = self.lockers[i - 1]
        self.lockers[index] = item
        self.num_lockers += 1
        print(f"Added locker {item} to the system at position {index}")
    
    ### REMOVE LOCKER FUNCTION ###
    def remove_locker(self, index):
        if index < 0 or index >= self.num_lockers:
            print("Error: Invalid locker position!")
            return
        for i in range(index, self.num_lockers - 1):
            self.lockers[i] = self.lockers[i + 1]
        self.lockers[self.num_lockers - 1] = None
        self.num_lockers -= 1
        print(f"Removed locker at position {index}")
    
    ### CHECK LOCKER FUNCTION ###
    def check_locker(self, index):
        if index < 0 or index >= self.num_lockers:
            print("Error: Invalid locker position!")
            return
        print(f"Locker at position {index} contains {self.lockers[index]}")
    
    ### EXPAND LOCKERS FUNCTION ###
    def _expand_lockers(self):
        new_capacity = 2 * self.capacity
        new_lockers = self._make_array(new_capacity)
        # Here we copy the lockers from the old array to the new array
        for i in range(self.num_lockers):
            new_lockers[i] = self.lockers[i]
        self.lockers = new_lockers
        self.capacity = new_capacity
        print(f"Lockers expanded to {new_capacity} lockers")
    
    ### DISPLAY LOCKERS FUNCTION ###
    def __str__(self):
        return f"Current lockers: {[self.lockers[i] for i in range(self.num_lockers)]}"

''' /*---+---+---+--End of Locker Class Block---+---+---+--*/ '''


''' /*---+---+---+--Start of user interface Block---+---+---+--*/ '''

def menu():
    locker_system = SchoolLockerSystem()
    while True:
        print("\n--- School Locker System ---")
        print("1. Add Locker")
        print("2. Insert Locker")
        print("3. Remove Locker")
        print("4. Check Locker")
        print("5. Display Lockers")
        print("6. Exit")
        choice = input("Please enter your choice: ")
        
        if choice == '1':
            item = input("Please enter the item to add to the locker: ")
            locker_system.add_locker(item)
        elif choice == '2':
            index = int(input("Please enter the position to insert the locker: "))
            item = input("Please enter the item to add to the locker: ")
            locker_system.insert_locker(index, item)
        elif choice == '3':
            index = int(input("Please enter the position to remove the locker: "))
            locker_system.remove_locker(index)
        elif choice == '4':
            index = int(input("Please enter the position to check the locker: "))
            locker_system.check_locker(index)
        elif choice == '5':
            print(locker_system)
        elif choice == '6':
            print("Exiting program...\n")
            break
        else:
            print("Invalid choice. Please try again.")
            
# Here we run or call the program
menu()

''' /*---+---+---+--End of user interface Block---+---+---+--*/ '''
