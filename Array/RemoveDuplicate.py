"""
How to remove Duplicate elements from an unsorted Array.

Input:
-------------
arr = [5, 1, 2, 6, 4, 4, 5]

Output:
---------
arr = [5, 1, 2, 6, 4]

"""
from collections import Counter

class Solution:
    def solve0(arr):
        l = []
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[i]!=arr[j]:
                    if arr[i] not in l:
                        l.append(arr[i])

        return l


    def solve(arr):
        l = []

        for i in arr:
            if i not in l:
                l.append(i)

        return l


    def solve1(arr):
        return list(set(arr))


    def solve2(arr):
        c = Counter(arr)
        return list(c.keys())


    def solve3(arr):
        c = Counter(arr)
        l = []

        for i in c.keys():
            l.append(i)

        return l

    def solve4(arr):
        arr.sort()

        for i in range(len(arr[1:])-1):
            if arr[i]==arr[i-1]:
                arr.remove(arr[i])
        
        return arr

    def solve5(l, arr):
        if len(arr)==0:
            return l

        if arr[0] not in l:
            l.append(arr[0])
            
        return Solution.solve5(l, arr[1:])


s = Solution
arr = [5, 1, 2, 4, 6, 4, 4, 5]
print(s.solve0(arr))
print(s.solve(arr))
print(s.solve1(arr))
print(s.solve2(arr))
print(s.solve3(arr))
print(s.solve4([5, 1, 2, 6, 4, 4, 5]))
print(s.solve5([], arr))