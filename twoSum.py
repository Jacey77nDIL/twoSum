class Solution(object):
    def twoSum(self, nums, target):  # LeetCode expects this method name exactly
        seen = {}  # Dictionary to track numbers we've already seen

        for i, num in enumerate(nums):
            second_num = target - num

            # Check if we've already seen the second number
            if second_num in seen:
                return [seen[second_num], i]  # Return the indices of the two numbers
            seen[num] = i  # Store the current number and its index
