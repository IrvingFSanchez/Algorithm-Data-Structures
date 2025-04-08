# Name: Irving F. Sanchez
# Course: Algorithm and Data Structures SP25-CPSC-34000-002
# School: Lewis University, Romeoville, IL
# Purpose: Implementation of a Doubly Linked List data structure with core operations

'''
Note: I put extensive comments in my code for personal use as they help me understand what
I'm doing and why I'm doing it. It's beneficial to reflect on the purpose behind each line of code.
'''

class DoublyLinkedList:
    # Inner Node class to represent elements in the list
    class Node:
        def __init__(self, data):
            self.data = data  # Store the node's data
            self.next = None  # Pointer to next node (initially None)
            self.prev = None  # Pointer to previous node (initially None)

    def __init__(self):
        self.head = None  # First node in the list
        self.tail = None  # Last node in the list
        self.size = 0     # Track number of elements (O(1) size check)

    def __len__(self):
        """Returns the current size of the list (O(1) operation)"""
        return self.size

    def is_empty(self):
        """Check if the list is empty (O(1) operation)"""
        return self.head is None

    def add_first(self, data):
        """
        Adds a new node with data at the beginning of the list (O(1) operation)
        If the list is empty, sets both head and tail to the new node.
        Otherwise, links the new node before the current head and updates head accordingly.
        """
        new_node = self.Node(data)
        if self.head is None:  # List is empty
            self.head = new_node
            self.tail = new_node
        else:
            # New node at the front should point to current first element (head)
            new_node.next = self.head
            # Update previous link of head's next to this new node
            self.head.prev = new_node
            # Move the head pointer to the new node
            self.head = new_node
        self.size += 1

    def add_last(self, data):
        """
        Adds a new node with data at the end of the list (O(1) operation)
        If the list is empty, sets both head and tail to the new node.
        Otherwise, links the new node after the current tail and updates tail accordingly.
        """
        new_node = self.Node(data)
        if self.tail is None:  # List is empty
            self.head = new_node
            self.tail = new_node
        else:
            # New node at the end should point to its predecessor (tail)
            new_node.prev = self.tail
            # Update next link of tail's previous to this new node
            self.tail.next = new_node
            # Move the tail pointer to the new node
            self.tail = new_node
        self.size += 1

    def remove_first(self):
        """
        Removes and returns the first node (O(1) operation)
        Handles edge cases where the list is empty or has only one element.
        """
        if self.head is None:  # Empty list case
            return
        if self.head == self.tail:  # Single element case
            self.head = None
            self.tail = None
        else:
            # Move head to next node, effectively removing the current first node
            self.head = self.head.next
            # Clear prev pointer of new head (not needed anymore)
            self.head.prev = None
        self.size -= 1

    def remove_last(self):
        """
        Removes and returns the last node (O(1) operation)
        Handles edge cases where the list is empty or has only one element.
        """
        if self.tail is None:  # Empty list case
            return
        if self.head == self.tail:  # Single element case
            self.head = None
            self.tail = None
        else:
            # Move tail to previous node, effectively removing the current last node
            self.tail = self.tail.prev
            # Clear next pointer of new tail (not needed anymore)
            self.tail.next = None
        self.size -= 1

    def delete(self, data):
        """
        Deletes the first occurrence of data in the list (O(n) operation)
        This method finds and removes a node with given data.
        It handles cases where the target is at head/tail or within the middle of the list.
        """
        current = self.head
        while current:
            if current.data == data:
                # If found, handle based on position in list
                if current == self.head:  # Data at head
                    return self.remove_first()
                elif current == self.tail:  # Data at tail
                    return self.remove_last()
                else:  # Data somewhere in the middle
                    # Bypass the node to be deleted by adjusting next and prev pointers
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.size -= 1
                    return  # Break after first deletion since it's O(n)
            current = current.next

    def display(self):
        """
        Prints the entire list from head to tail (O(n) operation)
        This method shows how elements are arranged in a doubly linked list.
        """
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")  # Indicate end of list

if __name__ == "__main__":
    # Test cases demonstrating functionality
    dll = DoublyLinkedList()
    # Basic operations
    dll.add_first(1)
    dll.add_first(2)
    dll.add_first(3)
    dll.display()  # Expected: 3 <-> 2 <-> 1 <-> None

    # Removal test
    dll.remove_first()
    dll.display()  # Expected: 2 <-> 1 <-> None

    # Additional operations
    dll.add_first(4) 
    dll.display()  # Expected: 4 <-> 2 <-> 1 <-> None

    # Deletion test
    dll.delete(2)
    dll.display()  # Expected: 4 <-> 1 <- None