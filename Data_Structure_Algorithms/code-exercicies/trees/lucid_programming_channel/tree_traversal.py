# Source: https://github.com/vprusso/youtube_tutorials/tree/master/data_structures/trees/binary_trees

class Stack(object):
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def size(self):
        return len(self.items)
    def __len__(self):
        return self.size()

class Queue(object):
    """
    To help Level-order Traversal
    """
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        """
        Ill return the top of the queue (the first in)
        """
        if not self.is_empty():
            return self.items[-1].value
    
    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        """
        Print out the tree with the type of algorithms (traversal_type) we ill print out 
        and call the function preorder_print
        """
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)
        elif traversal_type == "reverse_levelorder":
            return self.reverse_levelorder_print(tree.root)
        else:
            # Error check
            print("Traversal type" + str(traversal_type) + " is not supported")
            return False

    def preorder_print(self, start, traversal):
        """
        Print out the nodes of the tree
        Root -> Left -> Right
        """
        if start:
            traversal += (str(start.value) + "-")
            # Recursion, moves left and prints the current node
            traversal = self.preorder_print(start.left, traversal)
            # When all left, move to the right and start the process again
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """
        Print out the nodes of the tree
        Left -> Root -> Right
        """
        if start:
            # Ill recursevly check all left
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            # When no more left go to the right and go again check left
            traversal = self.inorder_print(start.right, traversal)
        
        return traversal

    def postorder_print(self, start, traversal):
        """
        Print out the nodes of the tree
        Left -> Right -> Root
        """
        if start:
            # Ill recursevly check all left
            traversal = self.postorder_print(start.left, traversal)
            # When no more left go to the right and go again check left
            traversal = self.postorder_print(start.right, traversal)
            # When get the left leaf print, when no more left leafs print right
            traversal += (str(start.value) + "-")
        return traversal

    def levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)
        
        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        
        return traversal

    def reverse_levelorder_print(self, start):
        if start is None:
            return
        
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"
        
        return traversal
    
    def height(self, node):
        """
        Gives the height of the tree
        """
        if node is None:
            return -1
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def size_(self, node):
        """
        Recursive way to get the size
        """
        if node is None:
            return 0
        
        return 1 + self.size_(node.left) + self.size_(node.right)

    def size(self):
        if self.root is None:
            return 0

        stack = Stack()
        stack.push(self.root)
        size = 1

        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)

        return size



tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

#         1                 height = 2
#       /   \
#      2       3            height = 1
#     / \     / \
#    4   5   6   7          height = 0

print(tree.print_tree("preorder"))
# 1-2-4-5-3-6-7-
print(tree.print_tree("inorder"))
# 4-2-5-1-6-3-7-
print(tree.print_tree("postorder"))
# 4-5-2-6-7-3-1-
print(tree.print_tree("levelorder"))
# 1-2-3-4-5-6-7-
print(tree.print_tree("reverse_levelorder"))
# 4-5-6-7-2-3-1-

print(tree.height(tree.root))
# 2
print(tree.size())
# 7
print(tree.size_(tree.root))
# 7

from queue import Queue

def convert_arr_to_binary_tree(arr):
    """
    Takes arr representing level-order traversal of Binary Tree 
    """
    index = 0
    length = len(arr)
    
    if length <= 0 or arr[0] == -1:
        return None

    root = BinaryTree(arr[index])
    index += 1
    queue = Queue()
    queue.put(root)
    
    while not queue.empty():
        current_node = queue.get()
        left_child = arr[index]
        index += 1
        
        if left_child is not None:
            left_node = BinaryTree(left_child)
            current_node.left = left_node
            queue.put(left_node)
        
        right_child = arr[index]
        index += 1
        
        if right_child is not None:
            right_node = BinaryTree(right_child)
            current_node.right = right_node
            queue.put(right_node)
    return root

def diameter_of_binary_tree(root):
    return diameter_of_binary_tree_func(root)[1]
    
def diameter_of_binary_tree_func(root):
    """
    Diameter for a particular BinaryTree Node will be:
        1. Either diameter of left subtree
        2. Or diameter of a right subtree
        3. Sum of left-height and right-height
    :param root:
    :return: [height, diameter]
    """
    if root is None:
        return 0, 0

    left_height, left_diameter = diameter_of_binary_tree_func(root.left)
    right_height, right_diameter = diameter_of_binary_tree_func(root.right)

    current_height = max(left_height, right_height) + 1
    height_diameter = left_height + right_height
    current_diameter = max(left_diameter, right_diameter, height_diameter)

    return current_height, current_diameter


def path_from_root_to_node(root, data):
    """
    Assuming data as input to find the node
    The solution can be easily changed to find a node instead of data
    :param data:
    :return:
    Given the root of a Binary Tree and a data value representing a node,
    return the path from the root to that node in the form of a list.
    You can assume that the binary tree has nodes with unique values.
    """
    output = path_from_node_to_root(root, data)
    return list(reversed(output))

def path_from_node_to_root(root, data):
    if root is None:
        return None

    elif root.data == data:
        return [data]

    left_answer = path_from_node_to_root(root.left, data)
    if left_answer is not None:
        left_answer.append(root.data)
        return left_answer

    right_answer = path_from_node_to_root(root.right, data)
    if right_answer is not None:
        right_answer.append(root.data)
        return right_answer
    return None