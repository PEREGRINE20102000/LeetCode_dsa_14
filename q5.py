#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst=[]
        if len(nums1)>len(nums2):
            for j in nums2:
                if j in nums1:
                    lst.append(j)


        else:
            for i in nums1:
                if i in nums2:
                    lst.append(i)
        return lst

"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ele={}
        for num in nums1:
            if num in ele:
               ele[num]+=1

            else:
                ele[num]=1

        lst=[]

        for num in nums2:
            if num in ele and ele[num]>0:
                lst.append(num)
                ele[num]-=1
        return lst