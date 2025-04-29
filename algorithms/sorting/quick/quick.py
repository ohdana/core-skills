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
    i = left + 1
    j = right
    partitioning_item = array[left]
    while True:
        while array[i] < partitioning_item:
            if i == right: break
            i += 1
        while partitioning_item < array[j]:
            if j == left: break
            j -= 1
            
        if i >= j: break
        array[i], array[j] = array[j], array[i]
        
    array[left], array[j] = array[j], array[left]
    
    return j
            

# testing

test_case_1 = [5, 1, 3, 2, 4]
expected_result_1 = [1, 2, 3, 4, 5]

test_case_2 = [3, 8, 1, 1, 5]
expected_result_2 = [1, 1, 3, 5, 8]

assert quick_sort(test_case_1) == expected_result_1
assert quick_sort(test_case_2) == expected_result_2