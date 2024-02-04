from typing import List

'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

input_list = [
    [1,2,3,1],
    [1,2,3,4],
    [1,1,1,3,3,4,3,2,4,2],
]

class Solution:
    def containsDuplicate(self , nums: List[int]) -> bool:

        final_list = set()

        for i in nums:
            if i in final_list:
                return True
            else:
                final_list.add(i)
        return False 

    def get_Duplicate(self , nums : List[int] ) -> bool:

        dict = {}

        for i in nums:
            if i not in dict:
                dict[u]



a = Solution()
for sample in input_list:
    print(a.containsDuplicate(sample))