"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
#Function Only

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        lst=set(nums)
        lst=list(lst)
        lst.sort()
        if lst==nums:
            return False
        elif lst!=nums:
            return True