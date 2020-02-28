#!/usr/bin/env python3
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Example: Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        array_len = len(nums)
        x = ((array_len) - 1 )
        for i in range(x):
            j = i + 1
            while j < (array_len):
                #if (nums[i] + nums[j]) == target:
                if (nums[i] + nums[j]) == target:
                    return[i,j]
                j = j + 1
sln = Solution()
result = sln.twoSum([2,7,11,15,6], 18)
print(result)

    