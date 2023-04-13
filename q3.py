#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i, num in enumerate(nums):
            remain=target-num
            if remain in seen:
                return [seen[remain],i]

            seen[num]=i
        return []



"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum=nums[i]+nums[j]
                if sum==target:
                    return [i,j]
"""