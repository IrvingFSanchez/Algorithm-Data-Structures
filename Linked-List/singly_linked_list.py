class SinglyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
        
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.head is None
    
    def add_first(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete(self, data):
        if self.head is None:
            return
        
        self.size -= 1

        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return    
            current = current.next

    def remove_first(self):
        if self.head is None:
            return
        
        self.head = self.head.next
        self.size -= 1

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')


# Test the Singly Linked List

if __name__ == '__main__':
    ll = SinglyLinkedList()

    ll.add_first(1)
    ll.add_first(2)
    ll.add_first(3)
    ll.display() # 3 -> 2 -> 1 -> None
    ll.remove_first()
    ll.display() # 2 -> 1 -> None

    ll.add_first(4)
    ll.display() # 4 -> 2 -> 1 -> None

    ll.delete(2)
    ll.display() # 4 -> 1 -> None