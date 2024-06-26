class Node:
    def __init__(self, data):
        # Initialize a node with data and next pointer
        self.data = data
        self.next = None

    def __str__(self):
        # Return a string representation of the node's data
        return str(self.data)

class SinglyLinkedList:
    def __init__(self):
        # Initialize an empty linked list with a head pointer
        self.head = None

    def list_size(self):
        # Helper method to get the size of the linked list
        tmp = self.head
        count = 0
        while tmp is not None:
            count += 1
            tmp = tmp.next
        return count

    def print_nodes(self):
        # Print the elements of the linked list
        if self.head is None:
            print("List is Empty!!")
            return
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end='->')
            tmp = tmp.next
        print('NULL')

    def insert_begin(self, newnode):
        # Insert a new node at the beginning of the linked list
        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = newnode
        else:
            # Connect the new node with the previous head and update the head
            newnode.next = self.head
            self.head = newnode

    def insert_end(self, newnode):
        # Insert a new node at the end of the linked list
        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = newnode
            return
        tmp = self.head
        while tmp.next is not None:
            # Traverse to the last node
            tmp = tmp.next
        # Update the next pointer of the last node to point to the new node
        tmp.next = newnode

    def insert_nth(self, newnode, pos):
        # Insert a new node at the specified position in the linked list
        if pos < 0:
            raise ValueError("Invalid Position!!")
        size = self.list_size()
        if pos > size:
            raise ValueError("Invalid Position!!")
        if pos == 0:
            # If inserting at position 0, set the new node as the head
            newnode.next = self.head
            self.head = newnode
            return
        i = 0
        tmp = self.head
        while i < pos - 1:
            # Traverse to the node before the desired position
            tmp = tmp.next
            i += 1
        # Insert the new node at the desired position
        newnode.next = tmp.next
        tmp.next = newnode

        # deletion of node

    def del_begin(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        # point head to node next
        self.head = self.head.next




# Initialization and testing
ll = SinglyLinkedList()
n1 = Node(5)
ll.head = n1
n2 = Node(10)
n1.next = n2
n3 = Node(15)
n2.next = n3
n4 = Node(25)
n3.next = n4
# ll.insert_nth(Node(200), 1)
# ll.insert_end(Node(500))
ll.del_begin()
ll.print_nodes()
