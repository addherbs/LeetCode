"""
Move Zeroes

Solution
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        n = len(nums)
        
        while zeros < n:
            if nums[zeros] == 0:
                break
            zeros += 1
            
        for i in range(zeros+1, n):
            if nums[i] != 0:
                nums[zeros], nums[i] = nums[i], nums[zeros]
                zeros += 1
        