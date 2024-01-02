import random
import numpy as n
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort


def test_bubble(array):
    print("Original Array: " + str(array))
    result = bubble_sort(array)
    print("Sorted Array: " + str(result))

    expected = array.copy()
    expected.sort()

    print("The array is sorted correctly") if (n.array(result) == n.array(expected)).all() else print("The array is not sorted correctly")


def test_insertion(array):
    print("Original Array: " + str(array))
    result = insertion_sort(array)
    print("Sorted Array: " + str(result))

    expected = array.copy()
    expected.sort()

    print("The array is sorted correctly") if (n.array(result) == n.array(expected)).all() else print("The array is not sorted correctly")


length = 20  # Set this value to whatever you wish

arr = []
for i in range(length):
    arr.append(random.randint(1, 100))
test_insertion(arr)
