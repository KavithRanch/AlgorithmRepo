''' SEARCHING ALGORITHMS
These are used to find whether an element exists within list/array
In this file, here are the algorithms detailed:
1. Linear Search               |     Worst Case Run-time: O(n)
2. Iterative Binary Search     |     Worst Case Run-time: O(log n)
'''


# ----------------------------------------------------------------------------------------------------

"LINEAR SEARCH searches from the first element in the array to the last"


# Checks in a sequential order whether each element in an array is our target and if so, return the index
# If we get to the end of the array, and we haven't found the target yet, return None
def linear_search(array, target):
    # For loop iterating through the indices of elements in the array
    for i in range(len(array)):
        if array[i] == target:
            return i

    return None


# ----------------------------------------------------------------------------------------------------

"BINARY SEARCH breaks down the search to smaller and smaller ranges until the element is found. "
"It wipes out half the searchable range by half every loop"


# Iterative implementation uses a while loop and updates the range to be smaller each loop
# Always checks whether the target is the middle value of the range, and if so return its index
# Also check whether our range doesn't include any more values, and is so return None
def binary_search_iterative(array, target):
    # Initialize lower boundary of range to be first element index, and upper boundary of range to be last element index
    lower_bound = 0
    upper_bound = len(array) - 1

    # While loop checking whether our range includes at least one value
    while upper_bound >= lower_bound:
        mid_value = (upper_bound + lower_bound) // 2  # Middle value will be halfway point between upper and lower

        if target == array[mid_value]:  # If the target value is equal to the middle element, return the index mid_value
            return mid_value
        elif target > array[mid_value]:  # If the target value > than middle element, update lower Bound value
            lower_bound = mid_value + 1
        else:  # If the target value < than middle element, update upper Bound value
            upper_bound = mid_value - 1

    # If the range no longer includes any values and the last remaining element wasn't the target, return None
    return None


# Recursive implementation calls itself with an updated and smaller range each call
# Always checks whether the target is the middle value of the range, and if so return its index
# Also check whether our range doesn't include any more values, and is so return None
def binary_search_recursive(lower_bound, upper_bound, array, target):  # Pre-condition: Array must be sorted (ascending)
    if upper_bound >= lower_bound:  # Checking whether our range includes at least one value
        mid_value = (lower_bound + upper_bound) // 2 # Middle value will be halfway point between upper and lower

        if target == array[mid_value]:  # If the target value is equal to the middle element, return the index mid_value
            return mid_value
        elif target > array[mid_value]:  # If target value > than middle element, call itself with lower bound updated
            return binary_search_recursive(mid_value + 1, upper_bound, array, target)
        else:  # If target value < than middle element, call itself with upper bound updated
            return binary_search_recursive(lower_bound, upper_bound - 1, array, target)
    else:  # If the range no longer includes any values and the last remaining element wasn't the target, return None
        return None


# ----------------------------------------------------------------------------------------------------



