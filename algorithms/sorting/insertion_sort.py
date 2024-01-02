"""INSERTION SORT sorts by finding where the current element fits in the sorted part of the array, moves it there"""


def insertion_sort(array):
    arr = array.copy()
    n = len(arr)
    for i in range(n):
        cur_val = arr[i]
        j = i - 1
        while j >= 0 and cur_val < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = cur_val

    return arr








