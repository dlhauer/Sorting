import math


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    for i in range(0, elements):
        if b == len(arrB):
            merged_arr[i:] = arrA[a:]
            break
        elif a == len(arrA):
            merged_arr[i:] = arrB[b:]
            break
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = math.ceil(len(arr) / 2)
    l_arr = merge_sort(arr[:mid])
    r_arr = merge_sort(arr[mid:])
    arr = merge(l_arr, r_arr)
    return arr

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
