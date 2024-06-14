# Refer to SOLUTIONS.md for the solution explanation.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Removes duplicates from a sorted singly linked list, e.g., [1, 1, 2, 2, 3, 4].

        Solution:
        You know when i wanted to solve this problem the first time, I used the approach of comparing adjacent nodes and if they are not equal i just update the next pointer, just as i would do if it was an Array, buh I now remembered in nodes their addresses are not known, so ...


        To solve the problem, we can just compare the adjacent nodes. If they are equal, we skip the next node by updating the next pointer 
        to point to the node after the next one. If they are not equal, we simply move to the next node.
        """
        tmp = head

        while tmp and tmp.next:
            if tmp.val == tmp.next.val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next

        return head

    def print_node(self, head: Optional[ListNode]) -> None:
        """
        Prints the values in the linked list from the given head node.
        """
        tmp = head

        while tmp:
            print(tmp.val, end=" --> ")
            tmp = tmp.next

        print("None")


def list_from_array(arr):

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

# Example usage:
sll = Solution()
arr = [1, 1, 2, 2, 3, 3, 4, 5]


head = list_from_array(arr)
sll.print_node(head)
new_head = sll.deleteDuplicates(head)
sll.print_node(new_head)
