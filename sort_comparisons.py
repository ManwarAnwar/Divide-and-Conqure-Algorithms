import random
import time
import sys
sys.setrecursionlimit(10000)  # increase limit for deep recursion on large arrays


# QUICK SORT IMPLEMENTATION

def quick_sort(arr):
    """Recursive Quick Sort (in-place, sorts in increasing order)."""
    def partition(low, high):
        pivot = arr[high]  # choose last element as pivot
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quicksort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort_recursive(low, pi - 1)
            quicksort_recursive(pi + 1, high)

    quicksort_recursive(0, len(arr) - 1)
    return arr


# MERGE SORT IMPLEMENTATION

def merge_sort(arr):
    """Recursive Merge Sort (returns a new sorted list)."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    """Helper function to merge two sorted lists."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# PERFORMANCE TEST FUNCTION

def test_sorting_algorithms():
    test_cases = {
        "Random": [random.randint(1, 10000) for _ in range(5000)],
        "Sorted": list(range(5000)),
        "Reverse Sorted": list(range(5000, 0, -1)),
    }

    for case, data in test_cases.items():
        print(f"\n--- {case} Data ---")

        # Test Quick Sort
        quick_data = data.copy()
        start = time.time()
        quick_sort(quick_data)
        end = time.time()
        print(f"Quick Sort Time: {end - start:.4f} seconds")

        # Test Merge Sort
        merge_data = data.copy()
        start = time.time()
        sorted_merge = merge_sort(merge_data)
        end = time.time()
        print(f"Merge Sort Time: {end - start:.4f} seconds")


# MAIN RUNNER

if __name__ == "__main__":
    test_sorting_algorithms()
