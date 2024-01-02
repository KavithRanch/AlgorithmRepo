"""INSERTION SORT sorts by finding where the current element fits in the sorted part of the array, moves it there"""


def insertion_sort(array):
    arr = array.copy()
    n = len(arr)
    for i in range(n):
        curIndex = i
        for j in range(i, -1, -1):
            if curIndex != j:
                if arr[curIndex] >= arr[j]:
                    break
                else:
                    temp = arr[curIndex]
                    arr[curIndex] = arr[j]
                    arr[j] = temp
                    curIndex = j

    return arr








