"""TERNARY SEARCH is an extension of binary search with two midpoints instead of one."""

# Recursive implementation calls itself with an updated and smaller range each call
# Always checks whether the target is the value at the first or second third of the range, and if so return its index
# Also check whether our range doesn't include any more values, and is so return None
def ternary_search(lower_bound, upper_bound, array, target):
    if upper_bound >= lower_bound:
        first_mid_value = lower_bound + ((upper_bound - lower_bound) // 3)
        second_mid_value = upper_bound - ((upper_bound - lower_bound) // 3)

        if target == array[first_mid_value]:
            return first_mid_value
        if target == array[second_mid_value]:
            return second_mid_value

        if target < array[first_mid_value]:
            return ternary_search(lower_bound, first_mid_value - 1, array, target)
        elif array[first_mid_value] < target < array[second_mid_value]:
            return ternary_search(first_mid_value + 1, second_mid_value - 1, array, target)
        else:
            return ternary_search(second_mid_value + 1, upper_bound, array, target)
    else:
        return None
