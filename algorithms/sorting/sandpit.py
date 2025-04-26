from random import randint
import time

from bubble.bubble import bubble_sort
from selection.selection import selection_sort
from insertion.insertion import insertion_sort
from shell.shell import shell_sort

def get_random_numbers(n):
    return [randint(0, n) for i in range(n)]

sorts = {
    'Bubble sort': bubble_sort,
    'Selection sort': selection_sort,
    'Insertion sort': insertion_sort,
    'Shell sort (Sedgewick)': shell_sort,
    }

for i in [500, 1000, 5000, 10000, 15000]:
    print(f'\nTESTING {i} ELEMENTS')
    random_array = get_random_numbers(i)
    
    for sort_name, sort in sorts.items():
        array = random_array[:]
        start = time.time()
        sort(array)
        end = time.time()
        print(f'{sort_name}: {round(end-start, 3)}s')