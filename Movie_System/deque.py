# Name: Irving F. Sanchez
# Course: Algorithm and Data Structures SP25-CPSC-34000-002
# School: Lewis University, Romeoville, IL
# Purpose: Implement a Deque (Double-Ended Queue) ADT.

# This imports the deque class from Python's collections module
from collections import deque
    # This class represents the ADT Deque (Double-Ended Queue)
class Deque:

    # This initializes an empty deque
    def __init__(self):
        # This is used in the main.py, the Deque object is initialized to store movies
        # Specifically, at fim_deque = Deque() in main.py
        # self._deque is an instance of collections.deque which will act as an internal deque that will store all the items
        self._deque = deque()

    # This adds an item to the back of the deque
    def append(self, item):
        # This is used in main.py, when movies are added to the deque using append
        # Specifically, at film_deque.append(flick) in main.py
        # Specifically, it calls the append method of collections.deque to add the item to the right end
        self._deque.append(item)

    # This removes and returns an item from the front of the deque
    def popleft(self):
        # This is used in the main.py which is a method used to recommend a movie
        # Specifically, at flick = fim_deque.popleft() in main.py
        # Specifically, it checks if deque is empty using is_empty and if it's not empty, it calls the popleft method from collections.deque to remove and return leftmost item
        if self.is_empty():
            raise IndexError("Deque is empty. Can't pop from an empty Deque, old sport!")
        return self._deque.popleft()

    # This checks if the deque is empty
    def is_empty(self):
        # This is in main.py and this method is used to check if the deque is empty before recommending a movie
        ''' Secifically, at
        if not film_deque.is_empty():
            flick = film_deque.popleft()
        '''
        # Specificaly, it returns True if the length of the internal deque is 0, otherwise it returns False
        return len(self._deque) == 0

    # This returns the number of items in the deque
    def size(self):
        # This is in main.py and this method is used to display the number of movies loaded
        # Specifically, at print(f"Movies Loaded: {film_deque.size()}")
        # Specifically, calls the len function on the internal deque to get its size
        return len(self._deque)
    
    # This makes the deque class iterable
    def __iter__(self):
        # This is in main.py and this method is implicitly used when iterating over the deque
        return iter(self._deque)

    def __len__(self):
        #This is in main.py, and this method is used to get the number of movies in deque
        # Specifically, at print(f"Total moving picture flix Loaded: {len(film_deque)}")
        # This returns the number of items in the deque
        return len(self._deque)
