# Source = https://www.youtube.com/watch?v=8kptHdreaTA

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """ Ill append new values to the double linked list """
        # first check if its is the first time of the linked list
        if self.head is None:
            # Create a new node
            new_node = Node(data)
            # point previous pointer to none (beggining of the list)
            new_node.prev = None
            # Points the head to new pointer
            self.head = new_node
        # If already started the list
        else:
            # Create a new node
            new_node = Node(data)
            # Use a variable that is the current node (trav)
            trav = self.head
            # Pass through the linked list until find the last element (None)
            while trav.next:
                trav = trav.next
            # The next pointer of the current node ill point to the new node
            trav.next = new_node
            # Find the last node, now point the new node that we create to the current
            new_node.prev = trav
            # And established this new node has the last elemetent of the list
            new_node.next = None

    def prepend(self, data):
        """ Ill add new node at the beggining of the list """
        # if is the beginning of the list
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        # If is the linked list is not empty
        else:
            # Create a new node
            new_node = Node(data)
            # Point the head of the linked list to the new node
            self.head.prev = new_node
            # Point the new node to the head of the linked list
            new_node.next = self.head
            # Assign the new header to the new node
            self.head = new_node
            # point the new node previous pointer to null (indicates beginning of the double linked list)
            new_node.prev = None

    def add_after_node(self, key, data):
        """ Ill add between nodes, after the key given """
        # Create a variable that is the current node
        trav = self.head
        # Iterate over linked list
        while trav:
            # If linked list only has one node ( A ->):
            if trav.next is None and trav.data == key:
                # Use the append method that we create, because is to append to the last element of the linked list
                self.append(data)
                return
            # If we found the keu
            elif trav.data == key:
                # Create new node
                new_node = Node(data)
                # Get the next node
                next_node = trav.next
                # Point the current node to the new node
                trav.next = new_node
                # Point the new_node to the next node
                new_node.next = next_node
                # Point new node prev pointer to current node
                new_node.prev = trav
                # Point pointer next previous to new node
                next_node.prev = new_node
            # Iterate over the loop
            trav = trav.next

    def add_before_node(self, key, data):
        """ Ill add between nodes, before the key given """
        # Create a variable that is the current node
        trav = self.head
        # Iterate until the end of the linked list
        while trav:
            # Situation that linked list only have one value
            if trav.prev is None and trav.data == key:
                # Use method already exists
                self.prepend(data)
                return
            # Found the key
            elif trav.data == key:
                # create a node
                new_node = Node(data)
                # Indicates last node that is where the current node is pointing
                last_node = trav.prev
                # Point last node to new node
                last_node.next = new_node
                # Point current node to new node
                trav.prev = new_node
                # Point new node to the current node
                new_node.next = trav
                # Point new node previous pointer to last node
                new_node.prev = last_node
            # Iterate over the linked list
            trav = trav.next

    def delete(self, key):
        """ Delete a element when find by key """
        # Create the variable to see the current node
        trav = self.head
        # iterate over the linked list until trav == None
        while trav:
            if trav.data == key and trav == self.head:
                # Case 1 (only one node in the linked list):
                if not trav.next:
                    # Eliminate trav
                    trav = None
                    # Eliminate Linked list
                    self.head = None
                    return
                
                # Case 2 (to nodes in the linked list, and eliminate head):
                else:
                    # Indicates the next node of the current node
                    next_node = trav.next
                    # Eliminate pointer of the current node
                    trav.next = None
                    # Eliminate linked current node
                    next_node.prev = None
                    # Finally eliminate current node
                    trav = None
                    # Change head to next node
                    self.head = next_node
                    return
            elif trav.data == key:
                # Case 3:
                # if we are eliminating in the middle of the linked list
                if trav.next:
                    # Indicate the next node
                    next_node = trav.next
                    # Indicates last node
                    last_node = trav.prev
                    # Point last node to next node
                    last_node.next = next_node
                    # Point next node to last node
                    next_node.prev = last_node
                    # killing the pointer that are doing nothing and Node
                    trav.next = None
                    trav.prev = None
                    trav = None
                    return
                # Case 4:
                # The case where we are eliminating the last node of the linked list
                else:
                    # Indicate the node before the one that we want to eliminate
                    last_node = trav.prev
                    # The last node is the end of the linked list now, so point to none
                    last_node.next = None
                    # Eliminate pointer and node
                    trav.prev = None
                    trav = None
                    return
            # Iterate over the loop
            trav = trav.next    

    def reverse(self):
        # Create a temporary pointer
        tmp = None
        # Create a variable that indicates the current node
        trav = self.head
        # iterate over the linked list
        while trav:
            # Indicates to the temporary pointer the previous pointer of the current node
            tmp = trav.prev
            # Next flip the current previous ponter 
            trav.prev = trav.next
            # Flip the current next pointer
            trav.next = tmp
            # Iterate over loop (normally is next but is reversing)
            trav = trav.prev
        # If final of the linked list (tmp = None)
        if tmp:
            # Change head of the linked list to the last element of the linked list
            self.head = tmp.prev

    def print_list(self):
        """ Ill print the list """
        # Create a variable that is the current node
        trav = self.head
        # While not in the head of the linked list, print
        while trav:
            print(trav.data)
            # Pass to the next node
            trav = trav.next

dllist = DoublyLinkedList()
dllist.prepend(0)

dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)

dllist.prepend(5)

dllist.add_after_node(1, 11)
dllist.add_after_node(2, 12)

dllist.add_before_node(1, 11)
dllist.add_before_node(2, 12)

dllist.delete(5)
dllist.delete(11)
# Doesnt exists in the linked list:
dllist.delete(6)
dllist.delete(4)
dllist.delete(12)

dllist.reverse()

dllist.print_list()