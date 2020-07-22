class Queue:
    def __init__(self, initial_size = 10):
        # Create an array of the size predifined
        self.arr = [0 for _ in range(initial_size)]
        # Indicate the next element in the queueu, the next FREE slot (the first element is 0)
        self.next_index = 0
        # Indicates the front of the queue ( -1 indicate no elements in the queue nothing to be removed)
        self.front_index = -1
        # Indicates current size of the queue
        self.queue_size = 0

    def enqueue(self, value):
        """ Adds data to the back of the queue """
        # Check if queueu full and update to new size
        if self.queue_size == len(self.arr):
            self._handle_queue_capacity_full()

        # Add value to queue
        self.arr[self.next_index] = value
        # Update size
        self.queue_size += 1
        # Update free slot, has wrap around the queue with module
        self.next_index = (self.next_index + 1) % len(self.arr)
        # Check if queue empty, and update front of the index
        if self.front_index == -1:
            self.front_index = 0

    def size(self):
        """ Returns the current size of the queue """
        return self.queue_size

    def is_empty(self):
        """ Add an `is_empty` method that returns `True` if the queue is empty and `False` otherwise """
        return self.size() == 0
    
    def front(self):
        """ Returns the value for the front element """
        # check if queue is empty
        if self.is_empty():
            return None
        return self.arr[self.front_index]

    def dequeue(self):
        """ Removes data from the front of the queue """
        # Check is queueu is empty
        if self.is_empty():
            # Resetting pointers
            self.front_index = -1
            self.next_index = 0
            # Nothing to remove
            return None
        
        # Dequeue front element, hold remove value
        value = self.arr[self.front_index]
        # Update front index
        self.front_index = (self.front_index + 1) % len(self.arr)
        # Update new size of the queue
        self.queue_size -= 1
        # Return removed value
        return value
        
    def _handle_queue_capacity_full(self):
        """ Increases the capacity of the array, for cases in which the queue would otherwise overflow """
        # Copy current array
        old_arr = self.arr
        # Create a new array and double the size
        self.arr = [0 for _ in range(2 * len(old_arr))]

        # Create an variabel to indicate the current index to copy
        index = 0
        # Copy all elements from front of queue (front-index) until end
        for i in range(self.front_index, len(old_arr)):
            self.arr[index] = old_arr[i]
            index += 1

        # Case: When the queue is wrapped, when front-index is ahead of next index
        for i in range(0, self.front_index):
            self.arr[index] = old_arr[i]
            index += 1

        # Reset Pointers
        self.front_index = 0
        self.next_index = index
        
