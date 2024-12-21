import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Benchmarking
def benchmark_quicksort():
    # Generate random data
    data = [random.randint(0, 1000000) for _ in range(1000000)]
    
    # Start the timer
    start_time = time.time()
    
    # Run the quicksort
    sorted_data = quicksort(data)
    
    # Stop the timer
    end_time = time.time()
    
    print(f"Quicksort took {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    benchmark_quicksort()
