# THe simple implementation of Bubble Sort

def Bubble_Sort(arr):
    # Traversing whole array
    for i in range(len(arr)):
        # Here we again traversing whole array
        for j in range(len(arr)-1):
            # Here we traversing each element with his next elements
            if arr[j]>arr[j+1]:
                # If left element is bigger than right element,
                # Then we are traversing elements with his adjacent elements
                arr[j], arr[j+1] = arr[j+1], arr[j]

    # After all we printing sorted array
    return arr


# Approach 2: This algorithm will run for O(n^2) even if the array is
# already sorted. For avoiding this, we can check if elements are swapped
# in each pass. We will break the loop in case they are not

# Time Complexity: O(n^2) - Average or Worst Case; O(n) - Best case [Array is already sorted]

# In upper sorting algorith takes thirty iteration for sorting this [2, 6, 1, 5, 3, 4]

# But in the following algorithm takes fifteen iteration for sorting same array
 # Actullay this both algorithm takes same iteration for sorting any algorithm but in first algorithm
 # they traverse whole array again and again whatever they fully sorted or not

# so that we apply a exist condition in following algorithm so if array sort fully then they check
# condition if condition is true then, this algorithm exist this for loop.


def Bubble_sort(arr):
    # Traversing whole array
    for i in range(len(arr)):
        # We add a tracker for loop condition.
        m = 0
        # Here we are again traverse the array.
        for j in range(len(arr)-1):
            # We check all array elements
            if arr[j]>arr[j+1]:
                # if left element is greater then right element 
                # then we swap those value at the same time
                arr[j], arr[j+1] = arr[j+1], arr[j]
                m += 1
        if m==0:
            return arr

    return arr



arr = [2, 6, 1, 5, 3, 4]
res = Bubble_Sort(arr)
print(res)