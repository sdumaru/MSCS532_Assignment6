""" Implementation of Deterministic Selection Algorithm (Median-of-Medians) """

import random
import timeit

def median_of_medians(array, k):
    """ Function to determine median in the array """
    if len(array) <= 5:
        return sorted(array)[k]  # Sort the array and return the k-th smallest element

    # Divide array into groups of 5 and find medians
    sublists = [array[i:i+5] for i in range(0, len(array), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]

    # Find the median of medians which serve as pivot element
    pivot_element = median_of_medians(medians, len(medians) // 2)

    # Partition the array around the median of medians
    low = [j for j in array if j < pivot_element]
    high = [j for j in array if j > pivot_element]
    pivot_count = len(array) - len(low) - len(high)

    # Recurrence based on the position of k
    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + pivot_count:
        return pivot_element
    else:
        return median_of_medians(high, k - len(low) - pivot_count)

def print_execution_times(array_name, index):
    """ Function to print execution times """
    timer_stmt = '''median_of_medians({0}, {1})'''
    times = timeit.repeat(stmt=timer_stmt.format(array_name, index), repeat=5, number=10000, globals=globals())
    print('Total execution time: ' + str(min(times)))

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

# print(median_of_medians(A, 0)) #should be 1
# print(median_of_medians(A, 7)) #should be 99
# print(median_of_medians(B, 4)) #should be 60
# print(median_of_medians(C, 3)) #should be 4
