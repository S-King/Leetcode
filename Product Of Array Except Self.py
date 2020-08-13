from typing import List


class Solution:
    def productExceptSelf_TwoArrays(self, nums: List[int]) -> List[int]:
        list_length = len(nums)
        if list_length == 0:
            return None
        elif list_length == 1:
            return 1

        # Create an array holding the sum of all items to the left of i
        L_array = [1]
        for i in range(1, list_length):
            L_array.append(L_array[i - 1] * nums[i-1])

        R_array = [1]
        reversed_list = nums[::-1]
        for i in range(1, list_length):
            R_array.append(R_array[i - 1] * reversed_list[i-1])
        R_array.reverse()

        output_array = []
        for i in range(list_length):
            output_array.append(R_array[i] * L_array[i])

        return output_array

    # This solution has the constraint of using constant space(the output array doesn't count towards the processing space)
    class Solution:
        def productExceptSelf_ConstantSpace(self, nums: List[int]) -> List[int]:
            list_length = len(nums)
            if list_length == 0:
                return None
            elif list_length == 1:
                return 1

            R_array = [1]
            running_total = 1
            reversed_list = nums[::-1]
            for i in range(1, list_length):
                R_array.append(R_array[i - 1] * reversed_list[i - 1])
            R_array.reverse()

            for i in range(list_length):
                R_array[i] = running_total * R_array[i]
                running_total = running_total * nums[i]

            return R_array


n = [1,2,3,4,5,6]

mySolution = Solution()
print(mySolution.productExceptSelf_TwoArrays(n))