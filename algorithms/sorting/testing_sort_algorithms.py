import random
import numpy as n
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort


def test_bubble(array):
    arr = array.copy()
    print("BUBBLE SORT:")
    print("Array: " + str(arr))
    result = bubble_sort(arr)
    print("Sorted Array: " + str(result))

    array.sort()

    print("The array is sorted correctly\n") if (n.array(result) == n.array(array)).all() else print("The array is not sorted correctly\n")


def test_insertion(array):
    arr = array.copy()
    print("INSERTION SORT:")
    print("Array: " + str(arr))
    result = insertion_sort(arr)
    print("Sorted Array: " + str(result))

    array.sort()

    print("The array is sorted correctly\n") if (n.array(result) == n.array(array)).all() else print("The array is not sorted correctly\n")


def test_selection(array):
    arr = array.copy()
    print("SELECTION SORT:")
    print("Array: " + str(arr))
    result = selection_sort(arr)
    print("Sorted Array: " + str(result))

    array.sort()

    print("The array is sorted correctly\n") if (n.array(result) == n.array(array)).all() else print("The array is not sorted correctly\n")


length = 20  # Set this value to whatever you wish

test_array = []
for i in range(length):
    test_array.append(random.randint(1, 100))

test_bubble(test_array)
test_insertion(test_array)
test_selection(test_array)
