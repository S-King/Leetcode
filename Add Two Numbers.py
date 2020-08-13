'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Fastest solution I could find
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, c=0) -> ListNode:
        # DUH, the smallest digits are first we can just mimic elementary math

        # Build the result on value at a time
        # C denotes if there was a carry over
        val = l1.val + l2.val + c

        # The possible values we are considering range from 0+0 to 9+9 or 0 to 18
        # If we divide the value by 10 using floor division (//) we get a 0 or 1 depending on the total
        c = val // 10
        val = val % 10

        # Now we have one val so lets create a node for it
        valueNode = ListNode(val=val)

        # Only move onto the next character if it exists
        # First time around I didn't think about the carry over with the final numbers
        if l1.next is not None or l2.next is not None or c != 0:
            # Now how are we going to move onto the next character?
            # If this is the last element on the chain for l1 we need to create another node to use in the recursive call
            # Then add it to the chain for l1
            if l1.next is None: l1.next = ListNode(val=0)
            if l2.next is None: l2.next = ListNode(val=0)
            valueNode.next = self.addTwoNumbers_TraverseLongestList(l1.next,l2.next,c=c)
        return valueNode






    def addTwoNumbers_TraverseLongestList(self, l1: ListNode, l2: ListNode) -> ListNode:

        # Lists must be non empty
        current_l1_node = l1
        current_l2_node = l2
        number1 = []
        number2 = []

        # There must be some length in common so use that to assign both
        while current_l1_node and current_l2_node is not None:
            number1.insert(0, current_l1_node.val)
            number2.insert(0, current_l2_node.val)

            current_l1_node = current_l1_node.next
            current_l2_node = current_l2_node.next

        # Now check is either of the numbers still needs to be finished reading into a variable
        while current_l1_node is not None:
            number1.insert(0, current_l1_node.val)
            current_l1_node = current_l1_node.next

        while current_l2_node is not None:
            number2.insert(0, current_l2_node.val)
            current_l2_node = current_l2_node.next

        # Convert int to strings
        number1 = "".join(map(str,number1))
        number2 = "".join(map(str,number2))

        # Coerce back to int and add
        total = int(number1) + int(number2)
        print("Answer is " + str(total))

        # Now must return this as a linked list
        previous_node = None
        for i in range(0, len(str(total))):
            print(str(total)[i])
            if previous_node == None:
                new_node = ListNode(val=int(str(total)[i]))
            else:
                new_node = ListNode(val=int(str(total)[i]), next=previous_node)
            previous_node = new_node
        return new_node



mySolution = Solution()
# In
# num1 = [2,4,3]
n1_node1 = ListNode(val=2)

n1_node2 = ListNode(val=4)
n1_node1.next = n1_node2

n1_node3 = ListNode(val=3)
n1_node2.next = n1_node3

# num2 = [5,6,4]
n2_node1 = ListNode(val=5)

n2_node2 = ListNode(val=6)
n2_node1.next = n2_node2

n2_node3 = ListNode(val=4)
n2_node2.next = n2_node3


# Out
# [7,0,8]
mySolution.addTwoNumbers_TraverseLongestList(n1_node1,n2_node1)