def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(i, len(arr)):
            smallest_index = j if arr[j] < arr[smallest_index] else smallest_index
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


def bubble_sort(arr):
    has_swapped = True
    end = len(arr) - 1
    while has_swapped:
        swap_count = 0
        for i in range(0, end):
            if arr[i] > arr[i+1]:
                swap_count += 1
                arr[i], arr[i+1] = arr[i+1], arr[i]
        has_swapped = True if swap_count > 0 else False
        end -= 1
    return arr

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
