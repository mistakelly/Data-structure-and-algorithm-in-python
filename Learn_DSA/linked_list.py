from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        # Return a string representation of the node's val
        return str(self.val)

class SinglyLinkedList:
    def __init__(self):
        # Initialize an empty linked list with a head pointer
        # self.head = None
        pass

    def list_size(self):
        # Helper method to get the size of the linked list
        tmp = self.head
        count = 0
        while tmp is not None:
            count += 1
            tmp = tmp.next
        return count

    def print_nodes(self, head):
        # Print the elements of the linked list
        if head is None:
            print("List is Empty!!")
            return
        tmp = head
        while tmp is not None:
            print(tmp.val, end='->')
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

    def del_begin(self, head):
        print('helllo from del begin')
        if head is None:
            print("List is empty. Nothing to delete.")
            return

        # point head to node next
        print('address of head', id(head))
        head = head.next
        self.print_nodes(head)

        return head

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # HELP ME GOD.


        if head is None:
            return None
        
        tmp = head

        while tmp and tmp.next:
            if tmp.val == tmp.next.val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        # tmp1, tmp2 = head1, head2

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # HELP ME GOD.

        if not list1: return list2
        
        if not list2: return list1
        # define head and tmp to None
        head = tmp = None
        while list1 and list2:
            if list1.val <= list2.val:
                if not head:
                    tmp = list1
                    head = tmp
                else:
                    tmp.next = list1
                    tmp = tmp.next
                list1 = list1.next
            else:
                if not head:
                    tmp = list1
                    head = tmp
                else:
                    tmp.next = list2
                    tmp = tmp.next
                list2 = list2.next


        tmp.next = list1 if list1 else list2

        return head









# construct node
def convert_array_to_node(arr):
        head = tmp = None
        for data in arr:
            new_node = ListNode(data)

            if head is None:
                head = new_node
                tmp = head
            else:
                tmp.next = new_node
                tmp = tmp.next


        return head

# Initialization and testing
ll = SinglyLinkedList()
# arr = [1, 1, 2, 2, 3, 3, 4, 5]

list1 = [1,2,4]
list2 = [1,3,4]

# list1 = [2]
# list2 = [1]


head1  = convert_array_to_node(list1)
head2 = convert_array_to_node(list2)

merged_head = ll.mergeTwoLists(head1, head2)
ll.print_nodes(merged_head)

# ll.print_nodes(head1)
# ll.print_nodes(head2)



