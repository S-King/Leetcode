from typing import List

'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

Constraints:
    The length of the array is in range [1, 20,000].
    The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # At each position sum up the previous positions until you get to your target or exceed it
        answer_array = []
        subarray_count = 0
        for i, num in enumerate(nums):
            # If we found the target then increase count and keep moving
            if num == k:
                subarray_count += 1
                continue
            # If the number is greater than k keep moving
            elif num > k: continue
            # Otherwise we need to look back at the other element for a sum
            # TRICK: note that range(0,0,-1) doesn't do anything so it just skips the first comparison, which is what we want
            running_sum = num
            for j in range(i-1,-1,-1):
                if nums[j] + running_sum > k: continue
                elif nums[j] + running_sum == k:
                    subarray_count += 1
                    break
                # At this point we know adding the number won't be over k so add it to the running total and move on
                else:
                    running_sum += nums[j]
        return subarray_count

    # The key here was to keep track of how many times each sum comes up
    # Then at each location check to see how many times we have (sum at i - k) since we can use these differences
    # to create a sequence. If the sum we are looking for appeared twice already, we can create two new sequences to
    # increment the answer by 2
    def subarraySum_HashTable(self, nums: List[int], k: int) -> int:
        sums = {0: 1}
        running_total = 0
        count = 0

        for value in nums:
            running_total += value

            # Need to see if the total where we are at minus the goal exists
            if sums.get(running_total - k):
                count += sums[running_total - k]
            if sums.get(running_total):
                sums[running_total] += 1
            else:
                sums[running_total] = 1
        return count


int_list = [0,25,25,50,-25,0,-25]
k = 2

mySolution = Solution()
mySolution.subarraySum(int_list, k)