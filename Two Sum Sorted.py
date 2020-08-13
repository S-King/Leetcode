from typing import List
# For timing answers
import time

''' 
Easy problem
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a 
specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where 
index1 must be less than index2.

Note:

    Your returned answers (both index1 and index2) are not zero-based.
    You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''

# First thoughts, it is sorted so we can binary search through it in O(log(n))
# There was a solutions that did some funky stuff with binary search but relied on a dictionary
# and binary search is hard to implement quickly and accurately so avoid it in timed situations if possible
class Solution:
    def two_sum_sorted_2Pointers(self, numbers, target):
        head = 0
        tail = len(numbers) - 1

        while head < tail:
            total = numbers[head] + numbers[tail]

            if total < target:
                head += 1
            elif total > target:
                tail -= 1
            elif total == target:
                return [head+1,tail+1] # +1's are bc they want them zero indexed
        return [-1,-1]



int_list = [2,7,11,15]
int_target = 9


mySolution = Solution()

# If there MUST be one and only one solution in this array then we can increment pointers down from both sides
# Think of it like a magnitude thing, if we can't make the target number using the smallest (left-most) number then
# you have to drop down a step on the largest (right-most side). If the answer could be in that bucket you can start
# trying each option, otherwise you'll have to step down another bucket of magnitude on the right
tic = time.perf_counter()
two_sum_sorted_2Pointers_solution = mySolution.two_sum_sorted_2Pointers(int_list, int_target)
toc = time.perf_counter()
print(two_sum_sorted_2Pointers_solution)
print(f"2 Pointers solution took {toc - tic:0.4f} seconds")


