class Node: 
    def __init__(self, key, parent = None): 
        self.key = key
        self.parent = parent 
        self.left = None  
        self.right = None
        
        if parent != None:
            if key < parent.key:
                assert (parent.left == None), 'parent already has a left child -- unable to create node'
                parent.left = self
            else: 
                assert key > parent.key, 'key is the same as parent.key. We do not allow duplicate keys in a BST since it breaks some of the algorithms.'
                assert (parent.right == None), 'parent already has a right child -- unable to create node'
                parent.right = self

    def get_leftmost_descendant(self):
        if self.left != None:
            return self.left.get_leftmost_descendant()
        else:
            return self

    def search(self, key):
        if self.key == key: 
            return (True, self)
        elif key < self.key:
            if self.left != None:
                return self.left.search(key)
            else:
                return (False, self)
        elif key > self.key:
            if self.right != None:
                return self.right.search(key)
            else:
                return (False, self)
    
    def insert(self, key):
        (found, parent) = self.search(key)
        if found:
            return (None, print("Key already exists"))
        else:
            new_node = Node(key, parent)
            return new_node
    
    def height(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.height()
        elif self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())
    
    # function to replace a node with its child or none (to be used in delete)
    def replace_node(self, new_node=None):
        if self.parent != None:
            if self.parent.left == self:
                self.parent.left = new_node
            else:
                self.parent.right = new_node
        if new_node != None:
            new_node.parent = self.parent

    # function to find the successor/leftMost descendent (node with smallest key in the right subtree) (to be used in delete)
    def find_successor(self):
        current = self.right
        while current.left != None:
            current = current.left
        return current
    
    def delete(self, key):
        (found, node_to_delete) = self.search(key)
        assert(found == True), f"key to be deleted:{key}- does not exist in the tree"
        
        if not found:
            return  print("Key not found, nothing to delete")

        # Case 1: Node has no children
        if node_to_delete.left == None and node_to_delete.right == None:
            node_to_delete.replace_node(None)

        # Case 2: Node has one child
        elif node_to_delete.left == None or node_to_delete.right == None:
            if node_to_delete.left != None:
                node_to_delete.replace_node(node_to_delete.left)
            else:
                node_to_delete.replace_node(node_to_delete.right)

        # Case 3: Node has two children
        else:
            successor = node_to_delete.find_successor()
            node_to_delete.key = successor.key
            successor.delete(successor.key)

#TEST CASES

t1 = Node(25, None)
t2 = Node(12, t1)
t3 = Node(18, t2)
t4 = Node(40, t1)

print('-- Testing basic node construction (originally provided code) -- ')
assert(t1.left == t2), 'test 1 failed'
assert(t2.parent == t1),  'test 2 failed'
assert(t2.right == t3), 'test 3 failed'
assert (t3.parent == t2), 'test 4 failed'
assert(t1.right == t4), 'test 5 failed'
assert(t4.left == None), 'test 6 failed'
assert(t4.right == None), 'test 7 failed'

# The tree should be : 
#             25
#             /\
#         12     40
#         /\
#     None  18
#

print('-- Testing search -- ')
(b, found_node) = t1.search(18)
assert b and found_node.key == 18, 'test 8 failed'
(b, found_node) = t1.search(25)
assert b and found_node.key == 25, 'test 9 failed -- you should find the node with key 25 which is the root'
(b, found_node) = t1.search(26)
assert(not b), 'test 10 failed'
assert(found_node.key == 40), 'test 11 failed -- you should be returning the leaf node which would be the parent to the node you failed to find if it were to be inserted in the tree.'

print('-- Testing insert -- ')
ins_node = t1.insert(26)
assert ins_node.key == 26, ' test 12 failed '
assert ins_node.parent == t4,  ' test 13 failed '
assert t4.left == ins_node,  ' test 14 failed '

ins_node2 = t1.insert(33)
assert ins_node2.key == 33, 'test 15 failed'
assert ins_node2.parent == ins_node, 'test 16 failed'
assert ins_node.right == ins_node2, 'test 17 failed'

print('-- Testing height -- ')

assert t1.height() == 4, 'test 18 failed'
assert t4.height() == 3, 'test 19 failed'
assert t2.height() == 2, 'test 20 failed'

print('Success: 15 points.')

# Testing deletion
t1 = Node(16, None)
# insert the nodes in the list
lst = [18, 25, 10, 14, 8, 22, 17, 12]
for elt in lst:
    t1.insert(elt)

# The tree should look like this
#               16
#            /     \
#          10      18
#        /  \     /  \
#       8   14   17  25
#          /         /  
#         12        22


# Let us test the three deletion cases.
# case 1 let's delete node 8
# node 8 does not have left or right children.
t1.delete(8)  # should have both children nil.
(b8, n8) = t1.search(8)
assert not b8, 'Test A: deletion fails to delete node.'
(b, n) = t1.search(10)
assert( b) , 'Test B failed: search does not work'
assert n.left == None, 'Test C failed: Node 8 was not properly deleted.'

# Let us test deleting the node 14 whose right child is none.
# n is still pointing to the node 10 after deleting 8.
# let us ensure that it's right child is 14
assert n.right != None, 'Test D failed: node 10 should have right child 14'
assert n.right.key == 14, 'Test E failed: node 10 should have right child 14'

# Let's delete node 14
t1.delete(14)
(b14, n14) = t1.search(14)
assert not b14, 'Test F: Deletion of node 14 failed -- it still exists in the tree.'
(b,n) = t1.search(10)
assert n.right != None , 'Test G failed: deletion of node 14 not handled correctly'
assert n.right.key == 12, f'Test H failed: deletion of node 14 not handled correctly: {n.right.key}'

# Let's delete node 18 in the tree. 
# It should be replaced by 22.

t1.delete(18)
(b18, n18) = t1.search(18)
assert not b18, 'Test I: Deletion of node 18 failed'
assert t1.right.key == 22 , ' Test J: Replacement of node with successor failed.'
assert t1.right.right.left == None, ' Test K: replacement of node with successor failed -- you did not delete the successor leaf properly?'

print('-- All tests passed: 15 points!--')
