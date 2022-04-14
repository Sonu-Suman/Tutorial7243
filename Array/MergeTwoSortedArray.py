"""
Given two sorted arrays, write a code to merge then in a sorted manner.

ex:
----
Input:
------------------
arr1 = {1, 5, 6, 7}
arr2 = {2, 5, 8, 9, 11}

Output:
------------------
arr = {1, 2, 5, 5, 6, 7, 8, 9, 11}

To solve this question in given Time complexity and Space complexity.
--> Time Complexity = O(n1+n2)
--> Space Complexity = O(n1+n2)
    Where:
    n1 :- number of elements present in arr1.
    n2 :- number of elements present in arr2.
"""
from InsertionSort import Solution

class SolutionMerge:
    def merge(self, arr1, arr2):
        l = []

        for i in arr1:
            l.append(i)
            l.sort()

        for j in arr2:
            l.append(j)
            l.sort()

        return l

    def merge1(self, arr1, arr2):
        arr1.extend(arr2)

        s = Solution.InsertionSort(arr1)
        return s

    def merge2(self, arr1, arr2):
        if len(arr1)==0:
            return arr2
        
        for i in arr1:
            arr2.append(i)

        return sorted(arr2)

    def merge_not_rapeatable(self, arr1, arr2):
        if len(arr1)==0:
            return arr2
            
        for i in arr1:
            if i not in arr2:
                arr2.append(i)

        return sorted(arr2)


s = SolutionMerge()
arr1 = [1, 5, 6, 7]
arr2 = [2, 5, 8, 9, 11]
print(s.merge(arr1, arr2))
arr1 = [1, 5, 6, 7]
arr2 = [2, 5, 8, 9, 11]
print(s.merge1(arr1, arr2))
arr1 = [1, 5, 6, 7]
arr2 = [2, 5, 8, 9, 11]
print(s.merge2(arr1, arr2))
arr1 = [1, 5, 6, 7]
arr2 = [2, 5, 8, 9, 11]
print(s.merge_not_rapeatable(arr1, arr2))