# Source : https://www.youtube.com/watch?v=5WoNhm7sOnA&list=PL5tcWHG-UPH3n5XGUN3nvENR7aFCV0gJr
# To check method is_circular_linked_list:
import linked_list as linked

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        # Create a new node
        new_node = Node(data)
        # Create the a variable that holds the current node
        trav = self.head
        # Point the new_node to the beggining of the list
        new_node.next = self.head

        # If no elements in the list
        if not self.head:
            new_node.next = new_node
        # When is atleast one element in the list
        else:
            # Iterate until the end of the cicle list
            while trav.next != self.head:
                trav = trav.next
            # In the end of the cicle list, point the current node to the new header (new_node)
            trav.next = new_node
        # Change head to the new_node
        self.head = new_node


    def append(self, data):
        """ Adding a new node in the end of the list """
        # If we dont have no node in the list (empty)
        if not self.head:
            # Create the first node
            self.head = Node(data)
            # Point the node to the head (circular)
            self.head.next = self.head
        # If already some node in the list
        else:
            # Create a new node
            new_node = Node(data)
            # Create a current variable to see node
            trav = self.head
            # Iterate over until the beginning of the cicle
            while trav.next != self.head:
                trav = trav.next
            # Find the last element of the cicle and add the new nde
            trav.next = new_node
            # Point the new node to the beginning of the cicle
            new_node.next = self.head
    
    def remove(self, key):
        """ Remove by value """
        # Case that the node that we want to remove is the head
        if self.head.data == key:
            # Create a variable to see current node
            trav = self.head
            # Iterate until the last node of the cicle
            while trav.next != self.head:
                trav = trav.next
            # Last element update to the head next (jumps)
            trav.next = self.head.next
            # And finally eliminates head
            self.head = self.head.next

        # Case that the node that we want to remove is not the head
        else:
            # Create a variable to see current node
            trav = self.head
            # Create a variable that ill be the previous node of the current node
            last_node = None
            # Iterate until the end of the cicle 
            while trav.next != self.head:
                # Indicates last node
                last_node = trav
                # Pass to the next node
                trav = trav.next
                # When find the key value
                if trav.data == key:
                    # Point last node to the next node
                    last_node.next = trav.next
                    # Eliminates current node
                    trav = trav.next

    def __len__(self):
        """" Overwriting the len function in python and count the lenght of the linked list """
        # Create a variabel current node
        trav = self.head
        # Create a count variable
        count = 0
        # Iterate until the end of the cicle
        while trav:
            # Add one every time we loop
            count += 1
            # To iterate over the list
            trav = trav.next
            # If end of the cicle
            if trav == self.head:
                break
        return count

    def split_list(self):
        """ Split the cicle linked list in the middle giving to cicle linked lists """
        # Gives size of the list
        size = len(self)
        # If no node in the list (size == 0), we cant split
        if size == 0:
            return None
        # If only one node in the list, we can split
        if size == 1:
            return self.head
        
        # General case
        # calculate midle of the cicle list
        mid  = size // 2
        # Create a count varible
        count = 0
        # Create a current node
        trav = self.head
        # Create a previous node of the current node
        last_node = None
        # Iterate over the list until find middle
        while trav and count < mid:
            # Count one more every loop
            count += 1
            # Refresh last node
            last_node = trav
            # To iterate
            trav = trav.next
        # Find the middle node and change pointer of the last node to the head
        last_node.next = self.head

        # Now construct the other half of the list
        split_cllist = CircularLinkedList()
        # Iterate until the head of the old cicle list
        while trav.next != self.head:
            # Every iteration that dont find the head, append to the new circular linked list
            split_cllist.append(trav.data)
            # To iterate over
            trav = trav.next
        # To get the last node
        split_cllist.append(trav.data)
        
        # To check if we did it
        self.print_list()
        print("\n")
        split_cllist.print_list()

    def is_circular_linked_list(self, input_list):
        """ Ill return true if is a circular linked list """
        # Create a variable to see current node
        trav = input_list.head
        # Iterate over until find the last element
        while trav.next:
            # To Iterate
            trav = trav.next
            # Check if the last element point to head (circular)
            if trav.next == input_list.head:
                return True
        # Dont find a circular linked list
        return False
    
    def iscircular(self, input_list):
        """   Determine wether the Linked List is circular or not
        Args:
        input_list(obj): Linked List to be checked
        Returns:
        bool: Return True if the linked list is circular, return False otherwise
        """
        if input_list.head is None:
            return False
        
        slow = input_list.head
        fast = input_list.head
        
        while fast and fast.next:
            # slow pointer moves one node
            slow = slow.next
            # fast pointer moves two nodes
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        # If we get to a node where fast doesn't have a next node or doesn't exist itself, 
        # the list has an end and isn't circular
        return False

    def print_list(self):
        """ Iterate over the cicle linked list and print """
        # Create a current variable
        trav = self.head
        # Iterate over until the end of the cicle, then break
        while trav:
            print(trav.data)
            # Iterate
            trav = trav.next
            # The break
            if trav == self.head:
                break

cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")

cllist.remove("B")
cllist.append("E")
print(len(cllist))
cllist.split_list()

llist = linked.linked_list()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.display()

print(cllist.is_circular_linked_list(cllist))
print(cllist.is_circular_linked_list(llist))
print(cllist.iscircular(cllist))
print(cllist.iscircular(llist))
