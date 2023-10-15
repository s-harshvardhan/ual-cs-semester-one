# First complete a minheap data structure.
# Please complete the missing code below.

class MinHeap:
    def __init__(self):
        self.H = [None]
 
    def size(self):
        return len(self.H)-1
    
    def __repr__(self):
        return str(self.H[1:])
        
    def satisfies_assertions(self):
        for i in range(2, len(self.H)):
            assert self.H[i] >= self.H[i//2],  f'Min heap property fails at position {i//2}, parent elt: {self.H[i//2]}, child elt: {self.H[i]}'
    
    def min_element(self):
        return self.H[1]

    ## bubble_up function at index
    def bubble_up(self, index):
        assert index >= 1 #make sure that the index is not the root node
        if index == 1:
            return
        # code up your algorithm here
        # your code here
        elif index > 1:
            for(i in range(index, len(self.H)))
                if self.H[i] < self.H[i//2]:
                    self.H[i] , self.H[i//2] = self.H[i//2] , self.H[i]
                else:
                    return
        elif index == 0:
            print("Can't enter at index 0")
            return
            

    ## bubble_down function at index
    def bubble_down(self, index):
        assert index >= 1 and index < len(self.H)
        lchild_index = 2 * index
        rchild_index = 2 * index + 1
        # code up your algorithm here
        # your code here

    # Function: heap_insert
    # Insert elt into heap
    # Use bubble_up/bubble_down function
    def insert(self, elt):
        # your code here

    # Function: heap_delete_min
    # delete the smallest element in the heap. Use bubble_up/bubble_down
    def delete_min(self):
        # your code here