""" Implementation of Deterministic Selection Algorithm (Median-of-Medians) """

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

A = [1, 25, 30, 4, 5, 1000, 8, 9, 99]
B = [15, 32, 43, 74, 56, 60]
C = [1, 2, 3, 4, 5]

print(median_of_medians(A, 0)) #should be 1
print(median_of_medians(A, 7)) #should be 99
print(median_of_medians(B, 4)) #should be 60
print(median_of_medians(C, 3)) #should be 4
