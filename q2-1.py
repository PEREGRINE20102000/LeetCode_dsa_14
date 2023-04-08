"""
Given an integer array nums, find the
subarray
 with the largest sum, and return its sum.
"""
#Function Only
#The last code only works if the max sum is positve

class solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum=nums[0]
        curSum=nums[0]
        for i in range(1, len(nums)):
            curSum=max(nums[i], curSum+nums[i])
            maxSum=max(maxSum, curSum)
        return maxSum
