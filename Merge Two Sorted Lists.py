'''
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing
together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(n+m), O(n+m)
    def mergeTwoLists_recursive(self, l1: ListNode, l2: ListNode) -> ListNode:
        # The key to recursions is identifying how to solve the next iteration then rerun the same problem on a subset

        if l1 is None: return l2
        if l2 is None: return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists_recursive(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_recursive(l1, l2.next)
            return l2



    # O(n+m) time, O(1) space
    def mergeTwoLists_singlePass(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode(-1)
        prev = head
        while l1 or l2 is not None:

            # If we have reached the end of linked list one, just append the rest of list two
            if l1 is None:
                prev.next = l2
                break
            if l2 is None:
                prev.next = l1
                break

            if (l1.val < l2.val):
                prev.next = l1
                prev = l1
                l1 = l1.next
                prev.next = None

            elif (l1.val >= l2.val):
                prev.next = l2
                prev = prev.next
                l2 = l2.next
                prev.next = None

        # head.next will be the lowest number
        return head.next