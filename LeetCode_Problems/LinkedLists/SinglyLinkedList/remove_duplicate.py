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

# Example usage:
sll = Solution()
node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(2)
node5 = ListNode(3)
node6 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

head = node1
sll.print_node(head)
new_head = sll.deleteDuplicates(head)
sll.print_node(new_head)
