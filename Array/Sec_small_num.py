# Finding the second smallest eleme
from InsertionSort import Solution

class SolutionSec:
    def solve0(self, arr):
        s0 = min(arr)
        s1 = s0
        s2= max(arr)
        for i in arr:
            if i<s2 and i>s0:
                s2 = i
                if s2!=s0:
                    s1 = i
        return s1


    def solve1(self, arr):
        s = Solution.InsertionSort(arr)
        i = 0
        c1 = s.count(s[0])
        return s[c1+1]


    def solve2(self, arr):
        arr.sort()
        c = arr.count(arr[0])
        return arr[c+1]


    
s = SolutionSec()
arr = [-1, 7, 1, 3, 4, 18, 1, -1, -1]
print(s.solve0(arr))
print(s.solve1(arr))
print(s.solve2(arr))