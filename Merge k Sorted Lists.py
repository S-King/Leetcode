from typing import List
from queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# A bunch of approaches for this problem
class Solution:
    # This just adds all the elements to a queue and then sorts them
    def mergeKLists_BruteForce(self, lists: List[ListNode]) -> ListNode:
        # Check edge cases
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]


        # Create a new  list with all the values
        val_list = []
        for node in lists:
            ptr = node
            while ptr is not None:
                val_list.append(ptr.val)
                ptr  = ptr.next
        val_list.sort()
        list_head = ptr = ListNode()
        for val in val_list:
            ptr.next = ListNode(val)
            ptr = ptr.next
        return list_head.next


    # When using max and mins it is usually helpful to use infinity, this can be invoked with float("inf") or float("-inf")
    def mergeKLists_kComparisons(self, lists: List[ListNode]) -> ListNode:
        final_list = ptr = ListNode()

        # Go through the list so long as it has len > 0
        # Create a list of indices to remove at the end of every run
        inf = float("inf")
        while len(lists) > 0:
            min_val = inf
            min_index = -1

            # Going in reverse allows you to pop as soon as an empty set is seen without worrying about shifting the index
            for i in range(len(lists)-1, -1, -1):
                if lists[i]:
                    if lists[i][0].val < min_val:
                        min_val = lists[i][0].val
                        min_index = i

                # If the list is empty pop it
                else:
                    lists.pop(i)
            # Now that we have the lowest value, add it to the final linked list and remove it from the list it was in
            if min_index != -1:
                lowest_node = lists[min_index].pop(0)
                lowest_node.next = None
                ptr.next = lowest_node
                ptr = ptr.next
        return final_list.next

    # Using PQ the insert and pop is O(log k) but finding the smallest node it always the root so O(1)
    def mergeKLists_priorityQueue(self, lists: List[ListNode]) -> ListNode:
        priority_queue = PriorityQueue()
        head = ptr = ListNode()

        class Wrapper:
            def __init__(self, node):
                self.node = node

            def __lt__(self, other):
                if self.node.val < other.node.val:
                    return True
                else:
                    return False

        # Add all the first nodes of the lists (if they exist)
        for list in lists:
            if list:
                priority_queue.put(Wrapper(list))

        while not priority_queue.empty():
            wrapper = priority_queue.get()

            ptr.next = wrapper.node
            ptr = ptr.next
            if ptr.next:
                priority_queue.put(Wrapper(ptr.next))

        return head.next

    # Finally the most impressive method would be noticing that this question is basically what merge sort does as it
    # is combining the previously split lists back into a single sorted list
    def mergeKLists_divideAndConquer(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        elif len(lists) == 1:
            return lists[0]

        middle = len(lists) // 2
        left = lists[:middle]
        right = lists[middle:]

        # This will continue to call until we have single element lists
        # Remember that unlike the other example (which inserts the values back into the original list) we need to
        # keep track of the heads of the lists to combine them
        left_head = self.mergeKLists_divideAndConquer(left)
        right_head = self.mergeKLists_divideAndConquer(right)

        list_head = self.merge_dc(left_head, right_head)
        return list_head

        # We only get here once we have reached single element lists and begin building back to the full list

    def merge_dc(self, left : List[ListNode], right : List[ListNode]):
        head = ptr = ListNode()
        while left and right:
            if left.val < right.val:
                ptr.next = left
                ptr = ptr.next
                left = left.next
                ptr.next = None
            else:
                ptr.next = right
                ptr = ptr.next
                right = right.next
                ptr.next = None
        # If we still have elements append them to the end
        while left:
            ptr.next = left
            ptr = ptr.next
            left = left.next
            ptr.next = None

        while right:
            ptr.next = right
            ptr = ptr.next
            right = right.next
            ptr.next = None
        return head.next










l1 = [ListNode(1), ListNode(4), ListNode(5)]
l1[0].next = l1[1]
l1[1].next = l1[2]

l2 = [ListNode(1), ListNode(3), ListNode(4)]
l2[0].next = l2[1]
l2[1].next = l2[2]

l3 = [ListNode(2), ListNode(4)]
l3[0].next = l3[1]

full_list = [l1,l2,l3]

mySolution = Solution()
# mySolution.mergeKLists_BruteForce(full_list)
# mySolution.mergeKLists_kComparisons(full_list)

l1 = ListNode(1)
l1.next =  ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next =  ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next =  ListNode(4)

full_list = [l1,l2,l3]

# mySolution.mergeKLists_priorityQueue()

mySolution.mergeKLists_divideAndConquer(full_list)