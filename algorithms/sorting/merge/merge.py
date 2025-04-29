def merge_sort(array):
    sort(array, 0, len(array) - 1)
    
    return array

def sort(array, left, right):
    if right <= left: return
    mid = left + (right - left) // 2
    sort(array, left, mid)
    sort(array, mid + 1, right)
    merge(array, left, mid, right)

def merge(array, left, mid, right):
    i = left
    j = mid + 1
    
    array_copy = array[:]
    for k in range(left, right + 1):
        if i > mid:
            array[k] = array_copy[j]
            j += 1
        elif j > right:
            array[k] = array_copy[i]
            i += 1
        elif array_copy[i] < array_copy[j]:
            array[k] = array_copy[i]
            i += 1
        else:
            array[k] = array_copy[j]
            j += 1

# testing

test_case_1 = [5, 1, 3, 2, 4]
expected_result_1 = [1, 2, 3, 4, 5]

test_case_2 = [3, 8, 1, 1, 5]
expected_result_2 = [1, 1, 3, 5, 8]

assert merge_sort(test_case_1) == expected_result_1
assert merge_sort(test_case_2) == expected_result_2