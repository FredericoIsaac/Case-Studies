# Source: https://www.youtube.com/watch?v=JlMyYuY1aXU
# Source: https://realpython.com/linked-lists-python/
# Creating a node class
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None  # The pointer initially points to nothing

# Creating the linked list ( a wrapper of the class Nodes)
class linked_list:
    def __init__(self):
        # The first node of the list (head)
        self.head = Node()

    def append(self, data): 
        """ Append a new node with the value of the parameter data to the linked_list (at the end) """
        # Create a new node
        new_node = Node(data)  
        # Create a variable to store the current node we are looking (trav)
        # Iniciate in the first node (head)
        trav = self.head
        # Iterate over which nodes until the last node that ill be the Node that has None
        while trav.next != None:
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
        new_node.next = self.head.next
        # Point head to new_node 
        self.head.next = new_node

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


    def length(self):
        """ Find the length of the linked_list """
        # Create a variable that ill iterate over the linked list (trav)
        # And iniciate in the first element of the linked_list
        trav = self.head
        # Create a variable to count the number of elements
        total = 0
        # Iterate over linked list until last element (last element has next = None, doesnt point to anymore nodes)
        while trav.next != None:
            # Increment total everytime we pass through a node
            total += 1
            # Iterate over Linked_list
            trav = trav.next
        return total

    def display(self):
        """ Display the current content of the list """
        # Create a list of elements that we see (for latter print)
        elems = []
        # Create a variable that ill be the current node we are looking at (trav)
        trav = self.head
        # Iterate over linked list until last element (last element has next = None, doesnt point to anymore nodes)
        while trav.next != None:
            # Iterate over linked_list
            trav = trav.next
            # Append to list what value is the current node
            elems.append(trav.data)
            
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
        while True:
            # If not exist the function update index
            trav_index += 1                              
            # iterate over next node
            trav = trav.next
            # checks if current index is the one we are looking for
            if trav_index == index:
                # Find the index we are looking for, return value of that node
                return trav.data  
            

    def traverse(self):
        """ Traversing means going through every single node """
        # Create a variable that indicates the current node we are looking at (trav)
        trav = self.head
        # Iterate over the linked list until find None (the end)
        while trav.next != None:
            trav = trav.next

    def erase(self, index):
        """ An delete function, ill delete a node in the target """
        # First check control if the index is in range of the linked_list
        if index >= self.length():
            print ("ERROR: 'Get' Index out of range!")
            return None
        # Create a variable that indicates the current index we are looking at
        trav_index = 0
        # Create a variable that indicates the current node we are looking at (trav)
        trav = self.head
        # Iteration over the linked_list
        while True:
            # Save the last node that we pass
            last_node = trav
            # iterate over next node
            trav = trav.next
            # checks if current index is the one we are looking for
            if trav_index == index:
                # We find the index, and ill "delete" the current node
                # Is just passing the last_node to the next_node
                last_node.next = trav.next
                return
            # If not exist the function update index
            trav_index += 1 
    
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

            
# Creating a variable that is the linked_list
my_list = linked_list()
my_list.append(5)
my_list.append(3)
my_list.display()
my_list.insertion(6)
my_list.insertion(9)
my_list.display()
print(my_list.length())
print("Element at the first index: {}".format(my_list.get(1)))
my_list.erase(1)
my_list.display()
my_list.insert_between_after(5, 0)
my_list.display()
my_list.reverse()
my_list.display()

# Creating a linked List with three nodes
# Create a linked_list
my_list2 = linked_list()
# Create a node
first_node = Node("a")
# Associate first node to head of the linked list
my_list2.head.next = first_node
# Create the other two nodes
second_node = Node("b")
third_node = Node("c")
# Link the nodes together to the head of the linked list(first_node)
first_node.next = second_node
second_node.next = third_node




