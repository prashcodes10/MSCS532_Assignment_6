import random
import time
import matplotlib.pyplot as plt

# Randomized Quickselect

def randomized_select(arr, k):
    nums = arr.copy()
    
    def quickselect(left, right, k_smallest):
        if left == right:
            return nums[left]
        
        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)
        
        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return quickselect(left, pivot_index - 1, k_smallest)
        else:
            return quickselect(pivot_index + 1, right, k_smallest)

    def partition(left, right, pivot_index):
        pivot_value = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot_value:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index
    
    return quickselect(0, len(nums) - 1, k - 1)

# Deterministic Median of Medians

def deterministic_select(arr, k):
    nums = arr.copy()
    
    def select(nums, k):
        if len(nums) <= 5:
            nums.sort()
            return nums[k]
        
        medians = []
        for i in range(0, len(nums), 5):
            group = sorted(nums[i:i+5])
            medians.append(group[len(group)//2])
        
        pivot = select(medians, len(medians)//2)
        
        lows = [x for x in nums if x < pivot]
        highs = [x for x in nums if x > pivot]
        pivots = [x for x in nums if x == pivot]
        
        if k < len(lows):
            return select(lows, k)
        elif k < len(lows) + len(pivots):
            return pivot
        else:
            return select(highs, k - len(lows) - len(pivots))
    
    return select(nums, k - 1)


# Utility Functions for Testing

def generate_arrays(size):
    """Generate random, sorted, and reverse-sorted arrays."""
    random_array = [random.randint(1, size) for _ in range(size)]
    sorted_array = list(range(1, size + 1))
    reverse_sorted_array = sorted_array[::-1]
    return random_array, sorted_array, reverse_sorted_array

def measure_time(func, arr, k):
    """Measure execution time of a selection function."""
    start = time.time()
    func(arr, k)
    end = time.time()
    return end - start


# Experimental Setup

sizes = [1000, 5000, 10000, 20000]  # array sizes to test
k_fraction = 0.5  # testing median
distributions = ["Random", "Sorted", "Reverse-sorted"]

# Store results
results = {dist: {"Randomized QS": [], "Deterministic MoM": []} for dist in distributions}

# Running experiments
for size in sizes:
    random_array, sorted_array, reverse_sorted_array = generate_arrays(size)
    k = int(size * k_fraction)
    
    arrays = [random_array, sorted_array, reverse_sorted_array]
    
    for arr, dist_name in zip(arrays, distributions):
        t_randomized = measure_time(randomized_select, arr, k)
        t_deterministic = measure_time(deterministic_select, arr, k)
        
        results[dist_name]["Randomized QS"].append(t_randomized)
        results[dist_name]["Deterministic MoM"].append(t_deterministic)


# Plotting the Results

plt.figure(figsize=(12, 6))

markers = {"Randomized QS": "o", "Deterministic MoM": "s"}
colors = {"Randomized QS": "blue", "Deterministic MoM": "red"}

for dist in distributions:
    plt.plot(sizes, results[dist]["Randomized QS"], marker=markers["Randomized QS"],
             color=colors["Randomized QS"], linestyle='-', label=f"Randomized QS ({dist})")
    plt.plot(sizes, results[dist]["Deterministic MoM"], marker=markers["Deterministic MoM"],
             color=colors["Deterministic MoM"], linestyle='--', label=f"Deterministic MoM ({dist})")

plt.xlabel("Array Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Performance Comparison: Randomized Quickselect vs Deterministic Median of Medians")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
