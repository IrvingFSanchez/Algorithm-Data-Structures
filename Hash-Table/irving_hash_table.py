# Name: Irving F Sanchez
# Course: Algorithm and Data Structures SP25-CPSC-34000-002
# School: Lewis University, Romeoville, IL
# Purpose: Build a metaphorical Hash Table from scratch using chaining to handle collisions.
# Metaphor Used: Brain Filing System 🧠 - where each key is a thought, and values are memories stored in mental drawers.

''' /*---+---+---+--Start of BrainFilingSystem Class Block---+---+---+--*/ '''

class BrainFilingSystem: # Hash Table Class
    """
    This is the metaphorical hash table - a cognitive filing system inside the brain.
    Each key is a though or concept (like "childhood family dog"), and each value is the memory or image linked to that thought.
    The brain has a fixed number of mental drawers (slots), and a filing logic (hash) helps determine where to store or 
    """
    

    def __init__(self, capacity=10):
        ''' This will initialize the brain with a fixed number of memory drawers, all starting as empty. '''
        self.drawer_count = capacity # Total drawers available in the brain
        self.memory_drawers = [None] * self.drawer_count # Each drawer is initially empty (None) essentially initializing the hash map list
        
        
    ''' /*---+---+---+--Start of Hash Function Block---+---+---+--*/ '''
    def hash(self, thought): # Here we compute hash
        '''
        The brain uses a filing logic to assign each thought to a specific drawer
        by turning it into a numeric memory location within bounds.
        '''
        return abs(hash(thought)) % self.drawer_count
    ''' /*---+---+---+--End of Hash Function Block---+---+---+--*/ '''
    
    
    ''' /*---+---+---+--Start of Store Memory Block---+---+---+--*/ '''
    def store_memory(self, thought, memory): # This is the put(key, value) function
        '''
        This function files a memory in the right mental drawer:
        - If the drawer is empty, it adds the memory.
        - If the thought already exists, it updates the memory.
        - Otherwise, it stores it alongside other thoughts in the same drawer (chaining).
        '''
        drawer_idx = self.hash(thought)
        if self.memory_drawers[drawer_idx] is None:
            self.memory_drawers[drawer_idx] = [(thought, memory)]
        else:
            for i, (existing_thought, _) in enumerate(self.memory_drawers[drawer_idx]):
                if existing_thought == thought:
                    self.memory_drawers[drawer_idx][i] = (thought, memory)
                    return
            self.memory_drawers[drawer_idx].append((thought, memory))
    ''' /*---+---+---+--End of Store Memory Block---+---+---+--*/ '''
    
    
    ''' /*---+---+---+--Start of Recall Memory Function Block---+---+---+--*/ '''
    def recall_memory(self, thought): # This is the get(key) function
        '''
        This function helps the brain retrieve a memory by searching the correct drawer
        for a match to the incoming thought
        '''
        drawer_idx = self.hash(thought)
        drawer = self.memory_drawers[drawer_idx]
        if drawer is not None:
            for existing_thought, memory in drawer:
                if existing_thought == thought:
                    return memory
        return None
    ''' /*---+---+---+--End of Recall Memory Function Block---+---+---+--*/ '''
    
    
    ''' /*---+---+---+--Start of Forget Memory Function Block---+---+---+--*/ '''
    def forget_memory(self, thought): # This is the remove(key) function
        '''
        The brain decides to forget a memory. If a drawer becomes empty after removal,
        it resets the drawer back to its original empty state.
        '''
        drawer_idx = self.hash(thought)
        drawer = self.memory_drawers[drawer_idx]
        if drawer is not None:
            for i, (existing_thought, _) in enumerate(drawer):
                if existing_thought == thought:
                    del drawer[i]
                    if not drawer:
                        self.memory_drawers[drawer_idx] = None
                    return True
        return False
    ''' /*---+---+---+--End of Forget Memory Function Block---+---+---+--*/ '''


    ''' /*---+---+---+--Start of Brain Summary Print Block---+---+---+--*/ '''
    def __str__(self):
        '''
        This will provide a breakdown of each mental drawer and what memories it holds.
        If a drawer is empty, we note that the thoughts have faded away
        '''
        summary = "\n Brain Memory Drawers (Hash Table):\n"
        for idx, drawer in enumerate(self.memory_drawers):
            drawer_status = f"Drawer {idx}: "
            if drawer is None:
                drawer_status += "Empty (Thoughts have faded away)"
            else:
                thoughts = [f"'{thought}' -> {memory}" for thought, memory in drawer]
                drawer_status += " | ".join(thoughts)
            summary += drawer_status + "\n"
        return summary
    ''' /*---+---+---+--End of Brain Summary Print Block---+---+---+--*/ '''
    
    
    ''' /*---+---+---+--End of Brain Summary Print Block---+---+---+--*/ '''
    

''' /*---+---+---+--Start of Test Block---+---+---+--*/ '''

if __name__ == "__main__":
    print("\n--- Standard Brain (Capacity: 10 Drawers) ---")
    brain = BrainFilingSystem()

    # Storing memories
    brain.store_memory("childhood dog", "Barked loudly at the mailman")
    brain.store_memory("first bike ride", "Wobbly but thrilling")
    brain.store_memory("math exam", "Total panic, zero recall")
    brain.store_memory("vacation", "Sunburns and ice cream")

    # Recalling one memory
    print("Recalling 'first bike ride':", brain.recall_memory("first bike ride"))

    # Forgetting one memory
    brain.forget_memory("math exam")

    # Print current brain contents
    print(brain)

    ''' /*---+---+---+--Start of Collision Test Block---+---+---+--*/ '''
    print("\n--- Tiny Brain (Capacity: 2 Drawers) - Collision Test ---")
    tiny_brain = BrainFilingSystem(capacity=2)

    tiny_brain.store_memory("sunset memory", "The sky turned gold at the beach")
    tiny_brain.store_memory("deep conversation", "Felt seen for the first time")
    tiny_brain.store_memory("childhood fear", "Afraid of thunder")
    tiny_brain.store_memory("favorite snack", "Hot Cheetos during cartoons")

    print(tiny_brain)
    ''' /*---+---+---+--End of Collision Test Block---+---+---+--*/ '''
        
''' /*---+---+---+--End of Test Block---+---+---+--*/ '''

