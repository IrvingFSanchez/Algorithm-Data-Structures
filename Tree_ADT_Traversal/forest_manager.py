# Name: Irving F. Sanchez
# Course: Algorithm and Data Structures SP25-CPSC-34000-002
# School: Lewis University, Romeoville, IL
# Purpose: Implementation of a General Tree ADT with multiple traversal methods

'''
NOTES FOR IMPLEMENTATION:
This tree implementation uses a recursive structure where each node can have multiple children.
The three traversal methods (preorder, postorder, breadth-first) demonstrate different ways
to process hierarchical data. This is fundamental for algorithms in compilers, file systems,
and AI decision trees.
'''

#==================== START OF TREE NODE CLASS DEFINITION ====================#

class TreeNode:
    
    '''This is a single node in the hierarchical tree structure.
    Each node contains data and maintains references to its parent and children.'''
    
    def __init__(self, payload):
        '''
        The constructor for tree nodes.
        @param payload; The data/value is stored in this node
        '''
        self.payload = payload # The data stored in the node
        self.parent_branch = None # This refers to the parent node (None for root node)
        self.child_branches = [] # This is a list of child nodes (empty for leaf nodes)
        
    def graft_child(self, new_sapling):
        '''
        This adds a child node to this node (analogous to grafting a branch)
        @param new_sapling: The node to add as a child
        '''
        
        new_sapling.parent_branch = self
        self.child_branches.append(new_sapling)
        
    def prune_child(self, dead_branch):
        '''
        This removes a child node from this node (similar to pruning a tree branch)
        @param dead_branch: The node to remove from children
        '''
        
        if dead_branch in self.child_branches:
            self.child_branches.remove(dead_branch)
            dead_branch.parent_branch = None
            
    def is_leaf_node(self):
        '''
        This checks if this node is a leaf (end of a branch)
        @return: True if no children, False otherwise
        '''
        return len(self.child_branches) == 0

#===================== END OF TREE NODE CLASS DEFINITION ====================#


#==================== START OF TREE CLASS DEFINITION ====================#

class TreeGrove:
    '''
    The main tree container class that manages the entire hiearchy structure.
    Furthermore, this provides various traversal methods to process the tree structure.
    '''
    
    def __init__(self, root_arbor):
        '''
        The constructor requires a root node to initialize the tree
        @param root_arbor: The root node of our tree structure
        '''
        self.root_arbor = root_arbor # The foundational node of our tree
        
    def explore_preorder(self, current_arbor):
        '''
        Preorder Traversal: Which processes current node before children
        @param current_arbot: Which is the node we're currently visiting
        '''
        if current_arbor is None:
            return
        
        # Here we process current node (root at first)
        print(current_arbor.payload, end=(", " if current_arbor != self.root_arbor else ""))
        
        # Hereafter recursively process each child node
        for i, sapling in enumerate(current_arbor.child_branches):
            if current_arbor == self.root_arbor and i == 0:
                print(",  ", end= "")
            self.explore_preorder(sapling)
            if i < len(current_arbor.child_branches) - 1:
                print(", ", end= "")
                
    def explore_postorder(self, current_arbor):
        '''
        Postorder Traversal: Processes children before current node
        @param current_arbor: The node we're currently visiting
        '''
        
        if current_arbor is None:
            return
        
        # First recursively process each child node
        for i, sapling in enumerate(current_arbor.child_branches):
            self.explore_postorder(sapling)
            print(", ", end= "")
            
        # Then we process current node (root last)
        print(current_arbor.payload, end=("" if current_arbor == self.root_arbor else ""))
        
    def explore_breadth_first(self):
        '''
        Breadth-first traversal: Processes nodes level by level.
        Which uses a queue (simulated with list) to track nodes
        '''
        
        if self.root_arbor is None:
            return
        
        # Initializes queue with root node
        node_queue = [self.root_arbor]
        first_node = True
        
        while node_queue:
            current_arbor = node_queue.pop(0) 
            
            # Format for a cleaner output
            if first_node:
                print(current_arbor.payload, end="")
                first_node = False
            else:
                print(f", {current_arbor.payload}", end="")
                
            # Adds all children to queue
            node_queue.extend(current_arbor.child_branches)

#===================== END OF TREE CLASS DEFINITION ====================#


#==================== START OF TESTING THE TREE CONSTRUCTION ====================#
def cultivate_sample_tree():
    '''
    Constructs the exact sample tree from the sample on the assignment diagram given to us
    '''
    
    #Here we create all the tree nodes
    oak_tree = TreeNode("A")
    birch = TreeNode("B")
    cedar = TreeNode("C")
    dogwood = TreeNode("D")
    elm = TreeNode("E")
    fig = TreeNode("F")
    willow_tree = TreeNode("G")
    hazel = TreeNode("H")
    ironwood = TreeNode("I")
    maple = TreeNode("J")
    
    #Here we assemble the tree structure
    oak_tree.graft_child(birch)
    oak_tree.graft_child(cedar)
    oak_tree.graft_child(dogwood)
    
    birch.graft_child(elm)
    birch.graft_child(fig)
    
    dogwood.graft_child(willow_tree)
    
    willow_tree.graft_child(hazel)
    willow_tree.graft_child(ironwood)
    willow_tree.graft_child(maple)
    
    return TreeGrove(oak_tree) # Returns the complete tree structure

#==================== END OF TESTING THE TREE CONSTRUCTION ====================#


#==================== START OF THE MAIN EXECUTION ====================#

if __name__ == "__main__":
    print (" === Tree Traversal Demo === \n")
    
    #Grow the sample tree here
    arboretum = cultivate_sample_tree()
    
    print("Preorder exploration:")
    arboretum.explore_preorder(arboretum.root_arbor)
    
    print("\n\nPostorder exploration:")
    arboretum.explore_postorder(arboretum.root_arbor)
    
    print("\n\nBreadth-first exploration:")
    arboretum.explore_breadth_first()
    
