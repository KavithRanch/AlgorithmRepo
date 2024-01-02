"""BUBBLE SORT sorts by going through a list, looking at two elements at once, and swapping them accordingly"""

def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


    return array