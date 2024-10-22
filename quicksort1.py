import random

# Deterministic QuickSort
def deterministic_quick_sort(arr):
    comparisons = [0]  # To track comparisons

    def quick_sort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            quick_sort(arr, low, pivot_index - 1)
            quick_sort(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        comparisons[0] += (high - low)  # Counting comparisons
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    quick_sort(arr, 0, len(arr) - 1)
    return comparisons[0]

# Randomized QuickSort
def randomized_quick_sort(arr):
    comparisons = [0]  # To track comparisons

    def quick_sort(arr, low, high):
        if low < high:
            pivot_index = randomized_partition(arr, low, high)
            quick_sort(arr, low, pivot_index - 1)
            quick_sort(arr, pivot_index + 1, high)

    def randomized_partition(arr, low, high):
        comparisons[0] += (high - low)  # Counting comparisons
        rand_pivot = random.randint(low, high)
        arr[high], arr[rand_pivot] = arr[rand_pivot], arr[high]  # Swap with random pivot
        return partition(arr, low, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    quick_sort(arr, 0, len(arr) - 1)
    return comparisons[0]

# Main function to test both variants
def analyze_quick_sort():
    arr = list(map(int, input("Enter the array elements (space-separated): ").split()))
    
    arr_copy = arr[:]  # Make a copy for randomized quicksort

    # Deterministic quicksort
    det_comparisons = deterministic_quick_sort(arr)
    print(f"Sorted array using Deterministic QuickSort: {arr}")
    print(f"Number of comparisons (Deterministic): {det_comparisons}")

    # Randomized quicksort
    rand_comparisons = randomized_quick_sort(arr_copy)
    print(f"Sorted array using Randomized QuickSort: {arr_copy}")
    print(f"Number of comparisons (Randomized): {rand_comparisons}")

if __name__ == "__main__":
    analyze_quick_sort()
