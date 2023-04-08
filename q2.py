"""
Given an integer array nums, find the
subarray
 with the largest sum, and return its sum.
"""
#Function Only

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxNum=0
        curNum=0
        for i in range(0, len(nums)):
            curNum=max(nums[i],curNum+nums[i])
            if curNum>maxNum:
                maxNum=curNum
            elif curNum<0:
                curNum=0
        return maxNum
