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
    if(left >= right):
        return
    partition_idx = partition(arr, left, right)
    quick_sort(arr, left, partition_idx - 1)
    quick_sort(arr, partition_idx + 1, right)

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
    pivot = arr[left]
    partition_idx = left + 1
    for i in range(left + 1, right + 1):
        if arr[i] < pivot:
            arr[i], arr[partition_idx] = arr[partition_idx], arr[i]
            partition_idx +=1
    arr[left], arr[partition_idx - 1] = arr[partition_idx - 1], arr[left]
    return partition_idx

print(quick_sort_driver([3,5,1,8,2,9,4]))