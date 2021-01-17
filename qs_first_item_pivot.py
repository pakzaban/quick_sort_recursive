"""Quick-sort using first item as pivot"""
def quick_sort_driver(arr):
    """Drives the recursive quick_sort function and returns the mutated array"""
    quick_sort(arr,0, len(arr) - 1)
    return arr

def quick_sort(arr, left, right):
    """
    Does not return. Mutates existing list.
    :param arr: the main array, a portion of which will be partitioned
    :param left: left boundary of subarray to be partitioned.
    :param right: right boundary of subarray to be partitioned.
    :return: None
    """
    if left >= right:
        return
    partition_index = partition(arr, left, right)
    quick_sort(arr, left, partition_index - 1)
    quick_sort(arr, partition_index + 1, right)

def partition(arr, left, right):
    """
    Does not return. Mutates existing list.
    :param arr: the main array, a portion of which will be partitioned
    :param left: left boundary of subarray to be partitioned.
    :param right: right boundary of subarray to be partitioned.
        partition_index is index between numbers that are smaller and bigger than pivot. A[partition_index] is in its rightful place.
        j is the index between partitioned and un-partitioned portions of subarray
    :return: None
    """
    pivot = arr[left] # simple case: first element of subarray is the pivot
    partition_index = left + 1

    for j in range(left + 1, right + 1):
        if arr[j] < pivot:
            arr[j], arr[partition_index] = arr[partition_index], arr[j] #swap
            partition_index += 1 #partition_index advances only if a swap is required for partitionning
    arr[left], arr[partition_index - 1] = arr[partition_index - 1], arr[left]
    return partition_index


print(quick_sort_driver([7, 2, 1, 6, 8, 5, 3, 4]))







