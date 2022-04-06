"""
Given an array consisting 0's, 1's and 2's. we have to
write a code to sort an array:

"""


class Solution:

    def solve(self, arr):
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[j]<arr[i]:
                    arr[j], arr[i] = arr[i], arr[j]
        return arr

    def solve1(self, arr):
        arr.sort()
        return arr


s = Solution()
arr = [0, 1, 1, 0, 1, 2, 0, 1, 2]
print(s.solve(arr))
print(s.solve1(arr))