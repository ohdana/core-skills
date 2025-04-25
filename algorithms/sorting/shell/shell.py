def shell_sort(array):
    h = len(array) // 2
    while h > 0:
        for i in range(h, len(array), h):
            j = i - h
            while j >= 0 and array[j] > array[j + h]:
                array[j], array[j + h] = array[j + h], array[j]
                j -= h
        h //= 2
        
    return array

# testing

test_case_1 = [5, 1, 3, 2, 4]
expected_result_1 = [1, 2, 3, 4, 5]

test_case_2 = [3, 8, 1, 1, 5]
expected_result_2 = [1, 1, 3, 5, 8]

assert shell_sort(test_case_1) == expected_result_1
assert shell_sort(test_case_2) == expected_result_2