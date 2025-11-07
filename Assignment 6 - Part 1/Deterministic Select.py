import random

# DETERMINISTIC SELECT

def deterministic_select(arr, k):
    """
    Returning the k-th smallest element (1-indexed)
    using the deterministic Median of Medians algorithm.
    Guaranteeing O(n) worst-case performance.
    """
    nums = arr.copy()
    
    def select(nums, k):
        # Handling small arrays by sorting directly
        if len(nums) <= 5:
            nums.sort()
            return nums[k]
        
        # Splitting the array into groups of 5 and finding each median
        medians = []
        for i in range(0, len(nums), 5):
            group = sorted(nums[i:i+5])
            medians.append(group[len(group)//2])
        
        # Recursively finding the median of these medians
        pivot = select(medians, len(medians)//2)
        
        # Partitioning the array around this pivot
        lows = [x for x in nums if x < pivot]
        highs = [x for x in nums if x > pivot]
        pivots = [x for x in nums if x == pivot]
        
        # Checking which section contains the k-th element
        if k < len(lows):
            # Going into the left partition
            return select(lows, k)
        elif k < len(lows) + len(pivots):
            # Pivot itself is the answer
            return pivot
        else:
            # Going into the right partition
            return select(highs, k - len(lows) - len(pivots))
    
    # Adjusting k (turning 1-index into 0-index)
    return select(nums, k - 1)

# Example

if __name__ == "__main__":
    data = [7, 10, 4, 3, 20, 15, 4, 7]
    k = 4

    print(f"Array: {data}")
    print(f"{k}-th smallest (Deterministic Median of Medians): {deterministic_select(data, k)}")