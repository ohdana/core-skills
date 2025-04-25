from random import randint
import time

from bubble.bubble import bubble_sort as bubble
from selection.selection import selection_sort as selection
from insertion.insertion import insertion_sort as insertion
from shell.shell import shell_sort as shell

def get_random_numbers(n):
    return [randint(0, n) for i in range(n)]

sorts = {
    'Bubble sort': bubble,
    'Selection sort': selection,
    'Insertion sort': insertion,
    'Shell sort': shell,
    }

for i in [500, 1000, 5000, 10000]:
    print(f'\nTESTING {i} ELEMENTS')
    random_array = get_random_numbers(i)
    
    for sort_name, sort in sorts.items():
        array = random_array[:]
        start = time.time()
        sort(array)
        end = time.time()
        print(f'{sort_name}: {round(end-start, 3)}s')