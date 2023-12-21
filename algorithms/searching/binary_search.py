"""BINARY SEARCH breaks down the search to smaller and smaller ranges until the element is found. """
"It wipes out half the searchable range by half every loop and must receive a sorted array before commencing"


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