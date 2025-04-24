def selection_sort(array):
    for i in range(len(array)):
        min_element_index = i
        for j in range(i, len(array)):
            if array[j] < array[min_element_index]:
                array[min_element_index], array[j] = array[j], array[min_element_index]
    
    return array
        

# testing

test_case_1 = [5, 1, 3, 2, 4]
expected_result_1 = [1, 2, 3, 4, 5]

test_case_2 = [3, 8, 1, 1, 5]
expected_result_2 = [1, 1, 3, 5, 8]

assert selection_sort(test_case_1) == expected_result_1
assert selection_sort(test_case_2) == expected_result_2