""" Implementation of Randomized Selection Algorithm (Randomized Quickselect) """

import random

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

A = [1, 25, 30, 4, 5, 1000, 8, 9, 99]
B = [15, 32, 43, 74, 56, 60]
C = [1, 2, 3, 4, 5]

print(randomized_select(A, 0)) #should be 1
print(randomized_select(A, 7)) #should be 99
print(randomized_select(B, 4)) #should be 60
print(randomized_select(C, 3)) #should be 4
