# Source: https://www.youtube.com/watch?v=JlMyYuY1aXU
# Source: https://realpython.com/linked-lists-python/
# Creating a node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # The pointer initially points to nothing

# Creating the linked list ( a wrapper of the class Nodes)
class linked_list:
    def __init__(self):
        # The first node of the list (head)
        self.head = None

    def append(self, data): 
        """ Append a new node with the value of the parameter data to the linked_list (at the end) """
        # Create a new node
        new_node = Node(data)
        # Checks if empty list
        if self.head is None:
            self.head = new_node
            return  
        # Create a variable to store the current node we are looking (trav)
        # Iniciate in the first node (head)
        trav = self.head
        # Iterate over which nodes until the last node that ill be the Node that has None
        while trav.next:
            # While not in the last Node trav ill pass to the other node next
            # Represents that trav is now the node after him, where the current trav is pointing
            trav = trav.next
        
        # Where he found the last node and ill point the trav next to the node that we create
        trav.next = new_node

    def insertion(self, data):
        """ Insert a new node with the value of the parameter data to the linked_list (at the beggining) """
        # Create a new node
        new_node = Node(data)
        # Point new_node to the header of the linked list
        new_node.next = self.head
        # Point head to new_node 
        self.head = new_node

    def insert_between_after(self, target_data, data):
        """ Insert new node between after the target data  """
        # Create a new Node
        new_node = Node(data)
        # Create a variable to hold current position node
        trav = self.head
        # checks if linked_list empty, so it can put number between
        if not self.head:
            raise Exception("List is empty")
        
        # iterate over linked list
        while trav.next != None:
            trav = trav.next
            # checks if the present iterate was the same target data
            if trav.data == target_data:
                # when found point the node that we want to introduce to the next node in the line
                new_node.next = trav.next
                # the present node, the target point now to the new node
                trav.next = new_node
                return
        # Target_data not found
        raise Exception("Node with data '%s' not found" % target_data)

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        # If the list is empty 
        if self.head is None:
            self.head = Node(value)
            return
            
        if pos == 0:
            self.prepend(value)
            return

        index = 0
        node = self.head
        while node.next and index <= pos:
            if (pos - 1) == index:
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node
                return

            index += 1
            node = node.next
        else:
            self.append(value)

    def length(self):
        """ Find the length of the linked_list """
        # Create a variable that ill iterate over the linked list (trav)
        # And iniciate in the first element of the linked_list
        trav = self.head
        # Create a variable to count the number of elements
        total = 1
        # Checks if list empty
        if not self.head:
            return 0
        # Iterate over linked list until last element (last element has next = None, doesnt point to anymore nodes)
        while trav.next:
            # Iterate over Linked_list
            trav = trav.next
            # Increment total everytime we pass through a node
            total += 1
            
        return total

    def display(self):
        """ Display the current content of the list """
        # Create a list of elements that we see (for latter print)
        elems = []
        # Create a variable that ill be the current node we are looking at (trav)
        trav = self.head
        # Iterate over linked list until last element (last element has next = None, doesnt point to anymore nodes)
        while trav:
            # Append to list what value is the current node
            elems.append(trav.data)
            # Iterate over linked_list
            trav = trav.next

        print(elems)

    def get(self, index):
        """ Extracter function, that ill pull out a data point in the linked list """
        # First check control if the index is in range of the linked_list
        if index >= self.length():
            print ("ERROR: 'Get' Index out of range!")
            return None
        # Create a variable that indicates the current index we are looking at
        trav_index = 0
        # Create a variable that indicates the current node we are looking at (trav)
        trav = self.head
        # Iteration over the linked_list
        while trav.next:
            if trav_index == index:
                # Find the index we are looking for, return value of that node
                return trav.data  
            # If not exist the function update index
            trav_index += 1                              
            # iterate over next node
            trav = trav.next
            # checks if current index is the one we are looking for
                
    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        if self.head is None:
            return None

        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next

        raise ValueError("Value not found in the list.")      

    def traverse(self):
        """ Traversing means going through every single node """
        # Create a variable that indicates the current node we are looking at (trav)
        trav = self.head
        # Iterate over the linked list until find None (the end)
        while trav.next != None:
            trav = trav.next

    def erase(self, index):
        """ An delete function, ill delete a node in the target """
        # Create a variable that indicates the current node we are looking at (trav)
        trav = self.head

        # Checks if index is the head pointer
        if index == 0:
            # Point the head to the next index (1)
            self.head = trav.next
            # Eliminate node in the index 0
            trav = None
            return

        # Create a variable that indicates the index we are looking at
        trav_index = 0
        # Save the last node that we pass
        last_node = None

        # Iteration over the linked_list
        while trav and trav_index != index:
            # Save the last node that we pass
            last_node = trav
            # iterate over next node
            trav = trav.next
            # If not exist the function update index
            trav_index += 1 

        # checks if we reach the end of the list and dont find the index 
        if trav is None:
            return

        # We find the index, and ill "delete" the current node
        # Is just passing the last_node to the next_node
        last_node.next = trav.next
        # Then current eliminate current node
        trav = None          

    def remove(self, value):
        """ Delete the first node with the desired data. """
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next

        raise ValueError("Value not found in the list.")

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        if self.head is None:
            return None

        node = self.head
        self.head = self.head.next

        return node.value

    def reverse(self):
        """ Reverse a Linked List  A -> B -> C to A <- B <- C
        INCOMPLETE! APPEARS NONE IN THE FINAL AND SHOULD APPEAR THE LAST ELEMENT """
        # Create a variable that indicates the current node
        trav = self.head
        # Create variabel that hold te last node
        last_node = None
        # Iterate until the end of the list
        while trav:
            # Save current node pointer
            next_node = trav.next
            # Change pointer of the current node to point to the last node we have seen
            trav.next = last_node
            # Atualize last_node to current node
            last_node = trav
            # Continue to iterate
            trav = next_node
        # Change head to point to last node    
        self.head = last_node

    def merge_sorted(self, llist):
        # First list pointer
        p = self.head
        # Second list pointer
        q = llist.head
        # The pointer control
        s = None
        # checks empty lists
        if not p:
            return q
        if not q:
            return p
        
        # if lists not empty
        if p and q:
            # Check the to header list to see wich have low value
            if p.data <= q.data:
                # if p is smaller than q then s is p
                s = p
                # Atulize p to next node
                p = s.next
            # If q has a smaller number than p
            else:
                s = q
                q = s.next
            # Change head of the list to be s
            new_head = s
        # Iterate over the linked lists
        while p and q:
            # if p data is lower than q data
            if p.data <= q.data:
                # change pointer to lower p
                s.next = p
                # change s node
                s = p
                # Atualize p node to next node
                p = s.next
            # if q data is lower than p data
            else:
                # change pointer s to q
                s.next = q
                # change node to q
                s = q
                # Change node to q next
                q = s.next
        # When we arrive to the end of one of them
        if not p:
            # change pointer to the rest of the list that we have
            s.next = q
        if not q:
            # change pointer to the rest of the list that we have
            s.next = p

        # return the header of the new linked list
        return new_head

            
# Creating a variable that is the linked_list
my_list = linked_list()
my_list.append(5)
my_list.append(3)
my_list.display()
my_list.insertion(6)
my_list.insertion(9)
my_list.display()
print("Length of the list: {}".format(my_list.length()))
print("Element at the first index: {}".format(my_list.get(0)))
my_list.erase(3)
my_list.display()
my_list.insert_between_after(5, 0)
my_list.display()
my_list.reverse()
my_list.display()

# Creating a linked List with three nodes
# Create a linked_list
my_list2 = linked_list()
# Create a node
first_node = Node(0)
# Associate first node to head of the linked list
my_list2.head = first_node
# Create the other two nodes
second_node = Node(1)
third_node = Node(3)
# Link the nodes together to the head of the linked list(first_node)
first_node.next = second_node
second_node.next = third_node

my_list.display()
my_list2.display()
my_list.merge_sorted(my_list2)

my_list.display()
my_list2.display()





