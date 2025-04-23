def bubble_sort(array):
    for j in range(len(array)):
        for i in range(len(array) - 1):
            while array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array


# testing

test_case_1 = [5, 1, 3, 2, 4]
expected_result_1 = [1, 2, 3, 4, 5]

test_case_2 = [3, 8, 1, 1, 5]
expected_result_2 = [1, 1, 3, 5, 8]

assert bubble_sort(test_case_1) == expected_result_1
assert bubble_sort(test_case_2) == expected_result_2