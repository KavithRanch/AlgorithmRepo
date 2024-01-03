import random
import numpy as n
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort


def test_bubble(array, expected):
    bubble_arr = array.copy()
    print("BUBBLE SORT:")
    print("Array: " + str(bubble_arr))
    result = bubble_sort(bubble_arr)
    print("Sorted Array: " + str(result))

    print("The array is sorted correctly\n") if (n.array(result) == n.array(expected)).all() else print("The array is not sorted correctly\n")


def test_insertion(array, expected):
    insert_arr = array.copy()
    print("INSERTION SORT:")
    print("Array: " + str(insert_arr))
    result = insertion_sort(insert_arr)
    print("Sorted Array: " + str(result))

    print("The array is sorted correctly\n") if (n.array(result) == n.array(expected)).all() else print("The array is not sorted correctly\n")


def test_selection(array, expected):
    select_arr = array.copy()
    print("SELECTION SORT:")
    print("Array: " + str(select_arr))
    result = selection_sort(select_arr)
    print("Sorted Array: " + str(result))

    print("The array is sorted correctly\n") if (n.array(result) == n.array(expected)).all() else print("The array is not sorted correctly\n")


def test_merge(array, expected):
    merge_arr = array.copy()
    print("MERGE SORT:")
    print("Array: " + str(merge_arr))
    result = merge_sort(merge_arr)
    print("Sorted Array: " + str(result))

    print("The array is sorted correctly\n") if (n.array(result) == n.array(expected)).all() else print("The array is not sorted correctly\n")


length = 20  # Set this value to whatever you wish

test_array = []
for i in range(length):
    test_array.append(random.randint(1, 100))

ans = test_array.copy()

ans.sort()

test_bubble(test_array, ans)
test_insertion(test_array, ans)
test_selection(test_array, ans)
test_merge(test_array, ans)
