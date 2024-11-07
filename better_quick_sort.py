import random
import time

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

# Generate a random list for testing
data = random.sample(range(1, 1000), 100)

# Analyze deterministic quick sort
start_time = time.time()
sorted_deterministic = deterministic_quick_sort(data)
deterministic_time = time.time() - start_time
print("Deterministic Quick Sort Time:", deterministic_time)

# Analyze randomized quick sort
start_time = time.time()
sorted_randomized = randomized_quick_sort(data)
randomized_time = time.time() - start_time
print("Randomized Quick Sort Time:", randomized_time)
