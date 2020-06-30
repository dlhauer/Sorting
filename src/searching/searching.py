# STRETCH: implement Linear Search
def linear_search(arr, target):

    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid-1
        else:
            low = mid+1

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target):
    if len(arr) == 0:
        return -1
    start = 0
    end = len(arr)-1

    def helper(low, high):
        if low > high:
            return -1
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return helper(low, mid-1)
        elif arr[mid] < target:
            return helper(mid+1, high)
    return helper(start, end)
