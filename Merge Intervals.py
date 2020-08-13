from typing import List

class Solution:
    def merge_binary(self, intervals: List[List[int]]) -> List[List[int]]:
            # If we have two or less intervals we can
            if len(intervals) == 1:
                return intervals
            # Check if we should merge
            elif len(intervals) >= 2:
                split = len(intervals) // 2
                left = self.merge_binary(intervals[:split])
                right = self.merge_binary(intervals[split:])
                # Now combine left and right
                # This didn't work bc it didn't think about out of order pairs or intervals than enclose other intervals
                # if left[len(left)-1][1] >= right[0][0]:
                #     return [[left[0][0], right[len(right)-1][1]]]

                if ()


                else:
                    # Messed up here, append changes in place! Need to use +
                    return left + right









lists = [[1,3],[2,6],[8,10],[15,18]]


mySolution = Solution()
print(mySolution.merge_binary(lists))


