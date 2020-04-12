def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(i, len(arr)):
            smallest_index = j if arr[j] < arr[smallest_index] else smallest_index
        tmp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = tmp
    return arr


selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
