"""INSERTION SORT sorts by finding where the current element fits in the sorted part of the array, moves it there"""


def insertion_sort(array):
    arr = array.copy()
    n = len(arr)
    for i in range(n):
        for j in range(i, 0, -1):
            if arr[i] >= arr[j]:
                break
            else:








