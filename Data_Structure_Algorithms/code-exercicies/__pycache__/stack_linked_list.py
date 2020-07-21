# Add the Node class here
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None # No items in the stack, so head should be None
        self.num_elements = 0 # No items in the stack, so num_elements should be 0

    def push(self, value):
        """ Add elements to the top of the stack """
        # Create a node with the value
        new_node = Node(value)

        # Checks if stack is empty
        if self.head is None:
            self.head = new_node
        
        # Add the new node at the head of the linked list (top)
        else:
            # Point new_node to the head of the list
            new_node.next = self.head
            # Point the head to the new node so it is the start of the linked list
            self.head = new_node

        # Update number of elements on the stack
        self.num_elements += 1

    def size(self):
        """ Give the size of the stack """
        return self.num_elements
    
    def is_empty(self):
        """ Return true if empty stack """
        return self.num_elements == 0

    def pop(self):
        """ Eliminate and return first element of the stack """
        # Checks if stack empty if empty nothing to pop
        if self.is_empty():
            return None
        
        # Collect the value to return
        value = self.head.value
        # Eliminate top element
        self.head = self.head.next
        # Update number of elements on the stack
        self.num_elements -= 1

        # Return element eliminated
        return value