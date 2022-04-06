"""
find the duplicate array?
---------------------------
input = {1, 2, 5, 4, 2, 1, 4, 7}
-----------------------------------
Output = (1, 4}

we are going to use set data structure.
Set data structure is unordered collection of object and set is not allow 
enter duplicate element.


"""
from collections import Counter

class Solution:
    def solve(self, arr):
        s = set()
        l = []

        for i in arr:
            if i in s:
                l.append(i)
            s.add(i)

        return l


    def solve1(self, arr):
        c = Counter(arr)
        l = []

        for key, value in c.items():
            if value>1:
                l.append(key)

        return l


d = Solution()
arr = [1, 2, 5, 4, 1, 4, 3, 7]
print(d.solve(arr))
print(d.solve1(arr))

# This problem solve this type question in O(N) Time complexity.