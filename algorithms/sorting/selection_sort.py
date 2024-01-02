"""SELECTION SORT sorts by finding the smallest element in the array and moving it to the front of the array"""


def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_val = i
        for j in range(i, n):
            if array[j] < array[i]:
                min_val = j
        (array[i], array[min_val]) = (array[min_val], array[i])

    return array

