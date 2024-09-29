""" Implementation of Randomized Selection Algorithm (Randomized Quickselect) """

import random
import timeit

def randomized_select(array, k):
    """ Function to find the k-th smallest element in the array """
    array_size = len(array)
    if array_size == 1:
        return array[0]             # If the array is single element, return it

    # Randomly choose a pivot element
    pivot = random.choice(array)

    # Step 2: Partition the array around the pivot
    low = [i for i in array if i < pivot]
    high = [i for i in array if i > pivot]
    pivot_count = array_size - len(low) - len(high)

    # Step 3: Recur based on the position of k
    if k < len(low):
        return randomized_select(low, k)
    elif k < len(low) + pivot_count:
        return pivot
    else:
        return randomized_select(high, k - len(low) - pivot_count)

def print_execution_times(array_name, index):
    """ Function to print execution times """
    timer_stmt = '''randomized_select({0}, {1})'''
    times = timeit.repeat(stmt=timer_stmt.format(array_name, index), repeat=5, number=10000, globals=globals())
    print('Total execution time: ' + str(min(times)) + ' seconds')

def huge_random_array():
    """ Function to return huge number of random integers for testing purpose """
    array = []
    max_numbers = 500
    for _ in range(max_numbers):
        array.append(random.randint(0, max_numbers))
    return array

# Testing performance of algorithms on these arrays
randomized_array = [23, 65, 98, 1, 36, 47, 76, 28, 83, 15]
sorted_array = [1, 15, 23, 28, 36, 47, 65, 76, 83, 98]
reversed_sorted_array = [98, 83, 76, 65, 47, 36, 28, 23, 15, 1]
repeated_elements_array = [23, 56, 23, 84, 56, 23, 56, 84, 23, 84]

# Print execution times for the array
print("RANDOM ARRAY", end = " --> ")
print_execution_times(randomized_array, 6)

print("SORTED ARRAY", end = " --> ")
print_execution_times(sorted_array, 8)

print("REVERSED SORTED ARRAY", end = " --> ")
print_execution_times(reversed_sorted_array, 7)

print("REPEATED ELEMENTS ARRAY", end = " --> ")
print_execution_times(repeated_elements_array, 2)

print("HUGE RANDOM ARRAY", end = " --> ")
print_execution_times(huge_random_array(), 400)

# A = [1, 25, 30, 4, 5, 1000, 8, 9, 99]
# B = [15, 32, 43, 74, 56, 60]
# C = [1, 2, 3, 4, 5]

# print(randomized_select(A, 0)) #should be 1
# print(randomized_select(A, 7)) #should be 99
# print(randomized_select(B, 4)) #should be 60
# print(randomized_select(C, 3)) #should be 4
