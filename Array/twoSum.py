"""
Two sum problem (find pair with given sum in array.)

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice
ex-
Input:
-----------
arr = {2, 7, 11, 15}
target = 18

Output:
------------
(1, 2)

Explanation :
-----------------
arr[1] + arr[2] = 7+11 = 18

"""
from itertools import combinations

class Solution:
    # This is the first method
    # This take O(N^2)
    def TwoSum0(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return (i, j)
    

    # This is the second method
    # This take O(N)
    def TwoSum1(self, nums, target):
        for i in range(len(nums)-1):
            s = (target-nums[i])
            if s in nums[i+1:]:
                return i, nums.index(s)


    # This is the third method
    def TwoSum2(self, nums, target):
        l = []
        s = list(combinations(nums, 2))
        for i in s:
            if sum(list(i)) ==target:
                return nums.index(list(i)[0]), nums.index(list(i)[1])



s = Solution()
arr = [-1, 7, 1, 3, 4, 18]
t = 5
print(s.TwoSum0(arr, t))
print(s.TwoSum1(arr, t))
print(s.TwoSum2(arr, t))