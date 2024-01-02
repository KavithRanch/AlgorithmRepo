"""INSERTION SORT sorts by finding where the current element fits in the sorted part of the array, moves it there"""


def insertion_sort(array):
    n = len(array)
    for i in range(n):
        cur_val = array[i]
        j = i - 1
        while j >= 0 and cur_val < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = cur_val

    return array








