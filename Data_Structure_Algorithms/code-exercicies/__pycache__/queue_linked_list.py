class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:

    def __init__(self):
        # Attribute to keep track of the first node in the linked list
        self.head = None
        # Attribute to keep track of the last node in the linked list
        self.tail = None
        # Attribute to keep track of how many items are in the stack
        self.num_elements = 0

    def enqueue(self, value):
        # Create a new node with the value to introduce
        new_node = Node(value)
        # Checks is queue is empty
        if self.head is None:
            # If queue empty point both head and tail to the new node
            self.head = new_node
            self.tail = self.head
        else:
            # Add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail.next = new_node
            # Shift the tail (i.e., the back of the queue)  
            self.tail = self.tail.next  
        # Increment number of elements in the queue 
        self.num_elements += 1

    def dequeue(self):
        """ Eliminate first element of the queue and return that value """
        # Checks if queue empty, if empty nothing to dequeue
        if self.is_empty:
            return None
        
        # Save value of the element
        value = self.head.value

        # Shift head over to point to the next node
        self.head = self.head.next
        # Update number of elements
        self.num_elements -= 1
        # Return value that eliminate
        return value

    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0