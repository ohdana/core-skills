from random import shuffle

def quick_sort(array):
    shuffle(array)
    sort(array, 0, len(array) - 1)
    
    return array

def sort(array, left, right):
    if right <= left: return
    j = partititon(array, left, right)
    sort(array, left, j - 1)
    sort(array, j + 1, right)

def partititon(array, left, right):
    partition_item = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] <= partition_item:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]
    
    return i + 1

# testing

test_case_1 = [5, 1, 3, 2, 4]
expected_result_1 = [1, 2, 3, 4, 5]

test_case_2 = [3, 8, 1, 1, 5]
expected_result_2 = [1, 1, 3, 5, 8]

assert quick_sort(test_case_1) == expected_result_1
assert quick_sort(test_case_2) == expected_result_2