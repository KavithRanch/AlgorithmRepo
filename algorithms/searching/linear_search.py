"""LINEAR SEARCH searches from the first element in the array to the last"""

# Checks in a sequential order whether each element in an array is our target and if so, return the index
# If we get to the end of the array, and we haven't found the target yet, return None
def linear_search(array, target):
    # For loop iterating through the indices of elements in the array
    for i in range(len(array)):
        if array[i] == target:
            return i

    return None
