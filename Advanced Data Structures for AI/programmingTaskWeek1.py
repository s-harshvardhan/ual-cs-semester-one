class MinHeap:
    def __init__(self):
        self.H = [None]

    def size(self):
        return len(self.H) - 1

    def __repr__(self):
        return str(self.H[1:])

    def satisfies_assertions(self):
        for i in range(2, len(self.H)):
            assert self.H[i] >= self.H[i // 2], f'Min heap property fails at position {i // 2}, parent elt: {self.H[i // 2]}, child elt: {self.H[i]}'

    def min_element(self):
        return self.H[1]

    ## bubble_up function at index
    def bubble_up(self, index):
        assert index >= 1
        if index == 1:
            return

        while index > 1 and self.H[index] < self.H[index // 2]:
            self.H[index], self.H[index // 2] = self.H[index // 2], self.H[index]
            index = index // 2

    ## bubble_down function at index
    def bubble_down(self, index):
        assert index >= 1 and index < len(self.H)

        while (2 * index) < len(self.H):
            min_child_index = 2 * index
            if (2 * index + 1) < len(self.H) and self.H[2 * index + 1] < self.H[2 * index]:
                min_child_index = 2 * index + 1

            if self.H[index] <= self.H[min_child_index]:
                break

            self.H[index], self.H[min_child_index] = self.H[min_child_index], self.H[index]
            index = min_child_index

    # Function: heap_insert
    # Insert elt into heap
    # Use bubble_up/bubble_down function
    def insert(self, elt):
        self.H.append(elt)
        self.bubble_up(len(self.H) - 1)

    # Function: heap_delete_min
    # delete the smallest element in the heap. Use bubble_up/bubble_down
    def delete_min(self):
        if len(self.H) == 1:
            return None

        min_elt = self.H[1]

        # Replace the root with the last element
        self.H[1] = self.H[-1]
        self.H.pop()

        # Bubble down the new root to maintain the heap property
        self.bubble_down(1)

        return min_elt

class TopKHeap:
    # The constructor of the class to initialize an empty data structure
    def __init__(self, k):
        self.k = k
        self.A = []
        self.H = MinHeap()
        
    def size(self):
        return len(self.A) + self.H.size()
    
    def get_jth_element(self, j):
        assert 0 <= j < self.k
        assert j < self.size()
        return self.A[j]
    
    def satisfies_assertions(self):
        # is self.A sorted
        for i in range(len(self.A) - 1):
            assert self.A[i] <= self.A[i + 1], f'Array A fails to be sorted at position {i}, {self.A[i], self.A[i + 1]}'
        # is self.H a heap (check min-heap property)
        self.H.satisfies_assertions()
        # is every element of self.A less than or equal to each element of self.H
        for i in range(len(self.A)):
            assert self.A[i] <= self.H.min_element(), f'Array element A[{i}] = {self.A[i]} is larger than min heap element {self.H.min_element()}'

    # Function : insert_into_A
    # This is a helper function that inserts an element `elt` into `self.A`.
    # whenever size is < k,
    #       append elt to the end of the array A
    # Move the element that you just added at the very end of 
    # array A out into its proper place so that the array A is sorted.
    # return the "displaced last element" jHat (None if no element was displaced)    
    def insert_into_A(self, elt):
        assert (self.size() < self.k)
        self.A.append(elt)
        jHat = None
        j = len(self.A) - 1
        
        while j > 0 and self.A[j] < self.A[j - 1]:
            self.A[j], self.A[j - 1] = self.A[j - 1], self.A[j]
            jHat = self.A[j]
            j -= 1
        
        return jHat
    
    # Function: insert -- insert an element into the data structure.
    # Code to handle when self.size < self.k is already provided
    def insert(self, elt):
        size = self.size()
        # If we have fewer than k elements, handle that in a special manner
        if size < self.k:
            jHat = self.insert_into_A(elt)
            if jHat is not None:
                self.H.insert(jHat)
        else:
            minA = self.A[0]
            if elt < minA:
                self.H.insert(minA)
                self.A[0] = elt
                self.H.bubble_down(1)
            else:
                self.H.insert(elt)
    
    # Function: Delete top k -- delete an element from the array A
    # In particular delete the j^{th} element where j = 0 means the least element.
    # j must be in range 0 to self.k-1
    def delete_top_k(self, j):
        k = self.k
        assert self.size() > k
        assert 0 <= j < k
        
        deleted_element = self.A.pop(j)
        
        if self.H.size() > 0:
            maxA = self.A[0]
            minH = self.H.min_element()
            
            if minH < maxA:
                self.A[0] = minH
                self.H.delete_min()
            else:
                self.A[0] = self.H.delete_min()
        
        return deleted_element

