"""BUBBLE SORT sorts by going through a list, looking at two elements at once, and swapping them accordingly"""

def bubble_sort(array):
    arr = array.copy()
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


    return arr