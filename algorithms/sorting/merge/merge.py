def merge_sort(array):
    sort(array, 0, len(array) - 1)
    
    return array

def sort(array, lo, hi):
    if hi <= lo: return
    mid = lo + (hi - lo) // 2
    sort(array, lo, mid)
    sort(array, mid + 1, hi)
    merge(array, lo, mid, hi)

def merge(array, lo, mid, hi):
    i = lo
    j = mid + 1
    
    aux = array[:]
    
    for k in range(lo, hi + 1):
        if i > mid: 
            array[k] = aux[j]
            j += 1
        elif j > hi:
            array[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            array[k] = aux[j]
            j += 1
        else:
            array[k] = aux[i]
            i += 1

# testing

test_case_1 = [5, 1, 3, 2, 4]
expected_result_1 = [1, 2, 3, 4, 5]

test_case_2 = [3, 8, 1, 1, 5]
expected_result_2 = [1, 1, 3, 5, 8]

assert merge_sort(test_case_1) == expected_result_1
assert merge_sort(test_case_2) == expected_result_2