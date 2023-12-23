import random
from linear_search import linear_search
from binary_search import binary_search_iterative
from binary_search_recursive import binary_search_recursive
from ternary_search import ternary_search

def test_linear(array):
    print("LINEAR SEARCH:")
    print("Array: " + str(array))
    print("The value " + str(target) + " exists in the array at index " + str(linear_search(array, target)) + "\n") \
        if linear_search(array, target) is not None else (print("Element doesn't exist in the array\n"))


def test_iter_binary(array):
    array.sort()
    print("ITERATIVE BINARY SEARCH:")
    print("Array: " + str(array))

    print("The value " + str(target) + " exists in the array at index " + str(binary_search_iterative(array, target)) + "\n") \
        if binary_search_iterative(array, target) is not None else (print("Element doesn't exist in the array\n"))

def test_rec_binary(array):
    # Setting up bounds
    low = 0
    upper = length - 1

    array.sort()
    print("RECURSIVE BINARY SEARCH:")
    print("Array: " + str(array))

    print("The value " + str(target) + " exists in the array at index " + str(binary_search_recursive(low, upper, array, target)) + "\n") \
        if binary_search_recursive(low, upper, array, target) is not None else (print("Element doesn't exist in the array\n"))


def test_rec_ternary(array):
    # Setting up bounds
    low = 0
    upper = length - 1

    array.sort()
    print("RECURSIVE TERNARY SEARCH:")
    print("Array: " + str(array))

    print("The value " + str(target) + " exists in the array at index " + str(ternary_search(low, upper, array, target)) + "\n") \
        if ternary_search(low, upper, array, target) is not None else (print("Element doesn't exist in the array\n"))




length = 20  # Set this value to whatever you wish
target = 50

array = []
for i in range(length):
    array.append(random.randint(1, 100))

test_linear(array)
test_iter_binary(array)
test_rec_binary(array)
test_rec_ternary(array)