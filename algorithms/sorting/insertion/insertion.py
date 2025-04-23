def insertion_sort(array):
    for i in range(len(array)):
        j = i - 1
        while j >= 0 and array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            j -= 1
            
    return array

# testing

test_case_1 = [5, 1, 3, 2, 4]
expected_result_1 = [1, 2, 3, 4, 5]

test_case_2 = [3, 8, 1, 1, 5]
expected_result_2 = [1, 1, 3, 5, 8]

assert insertion_sort(test_case_1) == expected_result_1
assert insertion_sort(test_case_2) == expected_result_2