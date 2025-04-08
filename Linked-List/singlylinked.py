# Name: Irving F. Sanchez
# Course: Algorithm and Data Structures SP25-CPSC-34000-002
# School: Lewis University, Romeoville, IL
# Purpose: Implements and modifies a Singly Linked List with O(1) add_last()

'''Note: I put a ton of comments in my code for personal use, I add notes to help me understand what
I'm doing and why I'm doing it. I'm not sure if this is a good practice or not, but I'm doing it for now.
'''

class SinglyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    ''' /*---+---+---+--Start of SinglyLinkedList Class Block---+---+---+--*/ '''
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.head is None

    def add_first(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.size += 1

    def add_last(self, data):
        new_node = self.Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove_first(self):
        if self.head is None:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return removed_data

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    ''' /*---+---+---+--End of SinglyLinkedList Class Block---+---+---+--*/ '''

if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.add_first(1)
    ll.add_first(2)
    ll.add_first(3)
    ll.display()  # Output: 3 -> 2 -> 1 -> None
    ll.remove_first()
    ll.display()  # Output: 2 -> 1 -> None
    ll.add_first(4)
    ll.display()  # Output: 4 -> 2 -> 1 -> None
    ll.delete(2)
    ll.display()  # Output: 4 -> 1 -> None