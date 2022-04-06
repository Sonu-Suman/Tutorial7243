# This is a Insertion sorting algorithm


class Solution:
    def InsertionSort(arr):
        for j in range(len(arr)):
            m = 0
            for i in range(len(arr[j+1:])):
                if arr[i]>arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    m += 1
            if m==0:
                return arr

        return arr
        

# s = Solution()
# arr = [5, 4, 1, 2, 0, 1, 9]
# print(s.InsertionSort(arr))