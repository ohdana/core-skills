def insertion_sort_simple(array):
    for i in range(len(array)):
        j = i - 1
        while j >= 0 and array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            j -= 1
            
    return array

def insertion_sort_comparison_function(array, comparison_function):
    for i in range(len(array)):
        j = i - 1
        while j >= 0 and comparison_function(array[j], array[j + 1]) > 0:
            array[j], array[j + 1] = array[j + 1], array[j]
            j -= 1
            
    return array

# testing

test_case_1 = [5, 1, 3, 2, 4]
expected_result_1 = [1, 2, 3, 4, 5]

test_case_2 = [3, 8, 1, 1, 5]
expected_result_2 = [1, 1, 3, 5, 8]

test_case_3 = [(5, "apple"), (2, "banana"), (9, "cherry")]
expected_result_3 = [(2, "banana"), (5, "apple"), (9, "cherry")]

test_case_4 = [(3, "cat"), (3, "bird"), (2, "dog")]
expected_result_4 = [(2, "dog"), (3, "cat"), (3, "bird")]

assert insertion_sort_simple(test_case_1) == expected_result_1
assert insertion_sort_simple(test_case_2) == expected_result_2

def comparison_function_key_value_tuple(key_value_tuple_1, key_value_tuple_2):
    return int(key_value_tuple_1[0] > key_value_tuple_2[0])

assert insertion_sort_comparison_function(test_case_3, comparison_function_key_value_tuple) == expected_result_3
assert insertion_sort_comparison_function(test_case_4, comparison_function_key_value_tuple) == expected_result_4

class Obj:
    def __init__(self, prop):
        self.prop = prop
        
def comparison_function_obj(obj_1, obj_2):
    return int(obj_1.prop > obj_2.prop)

obj_1, obj_3, obj_5, obj_8 = Obj(1), Obj(3), Obj(5), Obj(8)
test_case_5 = [obj_3, obj_8, obj_1, obj_1, obj_5]
expected_result_5 = [obj_1, obj_1, obj_3, obj_5, obj_8]
assert insertion_sort_comparison_function(test_case_5, comparison_function_obj) == expected_result_5