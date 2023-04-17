"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

"""

#Brute Force

""" 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        num=-1
        lst1=[]
        lst2=[]
        for a in s:
            lst1.append(a)

        for i in lst1:
            if lst1.count(i)==1:
                lst2.append(lst1.index(i))
                num=lst2[0]

            
        return num
"""


def firstUniqChar(s: str) -> int:
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    for i in range(len(s)):
        if char_counts[s[i]] == 1:
            return i

    return -1
