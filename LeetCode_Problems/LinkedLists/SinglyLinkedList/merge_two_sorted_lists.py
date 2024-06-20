from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
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

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # HELP ME GOD.

        if not list1: return list2
        
        if not list2: return list1

        tmp = head = None

        while list1 and list2:
            if list1.val <= list2.val:
                if tmp is None:
                    tmp = list1
                    head = tmp  #hold the reference of tmp as tmp would be used to build the list
                else:
                    tmp.next = list1
                    tmp = tmp.next
                list1 = list1.next
            else:
                if tmp is None:
                    tmp = list2
                    head = tmp #hold the reference of tmp as tmp would be used to build the list
                else:
                    tmp.next = list2
                    tmp = tmp.next
                list2 = list2.next

        tmp.next = list1 if list1 else list2

        return head
    

class SinglyLinkedList:
    def __init__(self):
        # Initialize an empty linked list with a head pointer
        # self.head = None
        pass

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
ll = Solution()
# arr = [1, 1, 2, 2, 3, 3, 4, 5]

list1 = [1,2,4]
list2 = [1,3,4]

# list1 = [2]
# list2 = [1]


head1  = convert_array_to_node(list1)
head2 = convert_array_to_node(list2)

merged_head = ll.mergeTwoLists(head1, head2)
ll.print_nodes(merged_head)