# Creating a stack and there methods

# Create a class stack
class Stack:
    
    def __init__(self, initial_size = 10):
        # Fill the stack with 0 * 10 elements
        self.arr = [0 for _ in range(initial_size)]
        # Indicate the index of the current element of the stack
        self.next_index = 0
        # Indicate the current number of elements in the current stack
        self.num_elements = 0

    def push(self, data):
        """ Adds an item to the top of the stack """
        # Check if index out out of range
        if self.next_index == len(self.arr):
            print("Out of range! Increasing array capacity ...")
            # Increasing stack method
            self._handle_stack_capacity_full()
        # Insert new element in the current index
        self.arr[self.next_index] = data
        # Atualize index and number of elements 
        self.next_index += 1
        self.num_elements += 1
    
    def size(self):
        """ Return size of the stack """
        return self.num_elements

    def is_empty(self):
        """ Checks if stack is empty """
        return self.num_elements == 0

    def _handle_stack_capacity_full(self):
        """ Increase stack elements """
        # We ill create a new array of the old one because we need the reference of the elements
        old_arr = self.arr

        # Create a new array 2 times bigger
        self.arr = [0 for _ in range(2 * len(old_arr))]
        # Copying old references to the new array
        for index, element in enumerate(old_arr):
            self.arr[index] = element

    def pop(self):
        """ removes an item from the top of the stack (and returns the value of that item) """
        # Check if list is empty, if true return nothing to pop
        if self.is_empty():
            self.next_index = 0
            return None
        
        # Go to last element index - 1  and remove the last element
        self.next_index -= 1
        self.num_elements -= 1
        # return the element that as last to put in the stack
        return self.arr[self.next_index]