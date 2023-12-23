"""BINARY SEARCH breaks down the search to smaller and smaller ranges until the element is found."""
"It wipes out half the searchable range by half every loop and must receive a sorted array before commencing"


# Recursive implementation calls itself with an updated and smaller range each call
# Always checks whether the target is the middle value of the range, and if so return its index
# Also check whether our range doesn't include any more values, and is so return None
def binary_search_recursive(lower_bound, upper_bound, array, target):  # Pre-condition: Array must be sorted (ascending)
    n = len(array)
    if upper_bound >= lower_bound:  # Checking whether our range includes at least one value
        mid_value = lower_bound + (upper_bound - lower_bound) // 2  # Middle value will be halfway point between upper and lower

        if target == array[mid_value]:  # If the target value is equal to the middle element, return the index mid_value
            return mid_value
        elif target > array[mid_value]:  # If target value > than middle element, call itself with lower bound updated
            return binary_search_recursive(mid_value + 1, upper_bound, array, target)
        else:  # If target value < than middle element, call itself with upper bound updated
            return binary_search_recursive(lower_bound, mid_value - 1, array, target)
    else:  # If the range no longer includes any values and the last remaining element wasn't the target, return None
        return None
