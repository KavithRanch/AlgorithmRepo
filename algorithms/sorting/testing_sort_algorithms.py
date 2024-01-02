import random
import numpy as n
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort


def test_bubble(array):
    print("BUBBLE SORT:")
    print("Array: " + str(array))
    result = bubble_sort(array)
    print("Sorted Array: " + str(result))

    expected = array.copy()
    expected.sort()

    print("The array is sorted correctly\n") if (n.array(result) == n.array(expected)).all() else print("The array is not sorted correctly\n")


def test_insertion(array):
    print("INSERTION SORT:")
    print("Array: " + str(array))
    result = insertion_sort(array)
    print("Sorted Array: " + str(result))

    expected = array.copy()
    expected.sort()

    print("The array is sorted correctly\n") if (n.array(result) == n.array(expected)).all() else print("The array is not sorted correctly\n")


length = 20  # Set this value to whatever you wish

arr = []
for i in range(length):
    arr.append(random.randint(1, 100))

test_bubble(arr)
test_insertion(arr)
