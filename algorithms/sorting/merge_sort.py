"""MERGE SORT is a divide and conquer algorithm which breaks down the array recursively into smaller sub arrays.
Once each subarray is a single element, it begins to put each subarray array back together one by one in a sorted order,
each time merging into a larger array, until it results in the original array sorted

Typically implemented as one large function, here we see the two divide (mergesort()) and conquer (merge()) portions of
the algorithm implemented in separate functions"""


def merge(left, right):
    i = 0
    j = 0
    sort = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sort.append(left[i])
            i += 1
        else:
            sort.append(right[j])
            j += 1

    while i < len(left):
        sort.append(left[i])
        i += 1

    while j < len(right):
        sort.append(right[j])
        j += 1

    return sort


def merge_sort(array):
    n = len(array)
    if n > 1:
        mid = n // 2

        left_array = array[:mid]
        right_array = array[mid:]

        left_array = merge_sort(left_array)
        right_array = merge_sort(right_array)

        return merge(left_array, right_array)

    else:
        return array

