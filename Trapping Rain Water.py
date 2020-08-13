from typing import List
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of
rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''


class Solution:
    def trap(self, height: List[int]) -> int:

        # Initialize the array to store capacity to zeros
        water_capacity = [0] * len(height)
        print(water_capacity)

        for i, value in enumerate(height):
            if i == 0:continue
            if height[i] < height[i - 1]:
                water_capacity[i] = water_capacity[i - 1] + (height[i - 1] - height[i])

            if height[i] > height[i - 1]:
                # If the last space was able to hold water then we are in a fillable zone so we must change capacity
                if water_capacity[i-1] > 0:
                    if water_capacity[i - 1] + (height[i - 1] - height[i]) > 0:
                        water_capacity[i] = water_capacity[i - 1] + (height[i - 1] - height[i])
                    else:
                        water_capacity[i] = 0
                        # Otherwise it could just be a skyscraper
                else:
                    water_capacity[i] = 0

            if height[i] == height[i-1]:
                water_capacity[i] = water_capacity[i-1]

        # remember to account for beginning and end
        print(water_capacity)

        # now we have created our array lets see if we can use it to figure out trapping the water
        overall_total = 0
        running_total = 0
        for i,value in enumerate(water_capacity):
            if i == 0:continue
            elif value == 0:
                overall_total += running_total
                running_total = 0
            else:
                running_total += value

        print("Overall Total: {}".format(overall_total))
        return overall_total


    def trap_try2(self, height: List[int]) -> int:
        # Define a capacity based on the drop, ie if height drops 4 units
        # Everytime we go down we add one to the capacity pool
        # Everytime we go up we are allowed to add one unit from the capacity pool into the total

        print(height)
        print(height[::-1])
        forward_capacity = [0] * len(height)
        backward_capacity = [0] * len(height)

        print(forward_capacity)
        print(backward_capacity)

        total_rain = 0

        for i,value in enumerate(height):
            if i == 0: continue
            # Positive if going up , negative for going down
            change_in_altitude = height[i] - height[i-1]

            # If we are going down calculate the capacity for rain we are possibly getting
            if change_in_altitude < 0:
                forward_capacity[i] = forward_capacity[i-1] + (change_in_altitude * -1)

            # If we are going up we are losing any capacity we might have
            elif change_in_altitude > 0:
                # Get the increase in height from the last step, if we gained more height than we had capacity, out capacity is zero
                # Otherwise the capacity is reduced by the increase in height

                if change_in_altitude > forward_capacity[i-1]:
                    total_rain += forward_capacity[i-1]
                    forward_capacity[i] = 0
                else:
                    total_rain += change_in_altitude
                    forward_capacity[i] = forward_capacity[i-1] - change_in_altitude
            else:
                forward_capacity[i] = forward_capacity[i - 1]
                total_rain += forward_capacity[i - 1]

        # for i,value in enumerate(height[::-1]):
        #     if i == 0: continue
        #     # Positive if going up , negative for going down
        #     change_in_altitude = height[i] - height[i-1]
        #
        #     # If we are going down calculate the capacity for rain we are possibly getting
        #     if change_in_altitude < 0:
        #         backward_capacity[i] = backward_capacity[i-1] + height[i-1] - height[i]
        #
        #     # If we are going up we are losing any capacity we might have
        #     elif change_in_altitude > 0:
        #         # Get the increase in height from the last step, if we gained more height than we had capacity, out capacity is zero
        #         # Otherwise the capacity is reduced by the increase in height
        #         if change_in_altitude > backward_capacity[i-1]:
        #             backward_capacity[i] = 0
        #         else:
        #             backward_capacity[i] = backward_capacity[i-1] - change_in_altitude
        #     else:
        #         backward_capacity[i] = backward_capacity[i - 1]

        print("-" * 50)
        print(forward_capacity)
        print(backward_capacity)

        print("Total Rain: {}".format(total_rain))
        return total_rain


    def trap_minus1approach(self, height: List[int]) -> int:

        total_rain = 0
        accumulated_rain = 0
        # Go through and check for spots in the array that are between zeros, add 1 to the total rain count for each occurence
        between_zeros = False

        sum_of_heights = sum(height)

        while sum_of_heights > 0:
            for i,value in enumerate(height):
                if value > 0: between_zeros = True

                # Every time we hit a non zero value we can add any accumulated rain to the total
                if between_zeros == True and value > 0:
                    total_rain +=  accumulated_rain
                    accumulated_rain = 0
                elif between_zeros == True and value == 0:
                    accumulated_rain += 1

            # Now that we have all the accumulated rain from this round, de-increment the entire array by 1 and repeat
            # Don't forget to reset your variables!!
            height = [ value-1 if (value-1) >= 0 else 0 for value in height ]
            sum_of_heights = sum(height)
            between_zeros = False
            accumulated_rain = 0

        print(total_rain)
        return total_rain


    def trap_dynamicprogramming(self, height: List[int]) -> int:

        forward_backward = {}
        for direction in [1,-1]:
            capacity = [0] * len(height)
            max_capacity = 0

            for i, value in enumerate(height[::direction]):
                if value > max_capacity: max_capacity = value
                capacity[i] = max_capacity

            print (capacity)
            forward_backward[direction] = capacity
        print(forward_backward)

        # Now the tricky part, the places where the max values overlap are possible places where either water or dirt will be
        difference_array = [0] * len(forward_backward[1])
        for i,value in enumerate(forward_backward[1]):
            difference_array[i] = min(forward_backward[1][i], forward_backward[-1][i])

        print(difference_array)
        final_array = []
        for i,value in enumerate(difference_array):
            # Now finallwe we just need to remove any of the overlapping areas which are occupied by land
            final_array.append(difference_array[i] - height[i])

        print("height: {}".format(height))
        print("diff : {}".format(difference_array))
        print("Final: {}".format(final_array))
        print(sum(final_array))
        return sum(final_array)




    def trapwater_twopointers(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        # Create two pointers
        left_ptr = 0
        right_ptr = len(height) - 1
        left_max, right_max = height[left_ptr], height[right_ptr]
        total_water_collected = 0

        while left_ptr < right_ptr:

            if height[left_ptr] >= height[right_ptr]:

                if height[right_ptr] >= right_max:
                    right_max = height[right_ptr]
                else:
                    total_water_collected += right_max - height[right_ptr]
                right_ptr -= 1


            else:
                if height[left_ptr] >= left_max:
                    left_max = height[left_ptr]
                else:
                    total_water_collected += left_max - height[left_ptr]
                left_ptr += 1

        return total_water_collected


heights = [0,1,0,2,1,0,1,3,2,1,2,1]
# heights = [2,0,2]

mySolution = Solution()
# mySolution.trap(heights)
# mySolution.trap_try2(heights)
# mySolution.trap_minus1approach(heights)
mySolution.trapwater_twopointers(heights)