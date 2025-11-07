import random

# RANDOMIZED QUICKSELECT (Expected Linear Time)

def randomized_select(arr, k):
    """
    Returning the k-th smallest element (1-indexed)
    using Randomized Quickselect — expected linear time.
    """
    nums = arr.copy()  
    
    def quickselect(left, right, k_smallest):
        # Returning if down to one element
        if left == right:
            return nums[left]
        
        # Choosing a random pivot to avoid worst-case patterns
        pivot_index = random.randint(left, right)
        
        # Partitioning the array around the pivot
        pivot_index = partition(left, right, pivot_index)
        
        # Checking where the pivot lands relative to k
        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            # Recursing into the left side
            return quickselect(left, pivot_index - 1, k_smallest)
        else:
            # Recursing into the right side
            return quickselect(pivot_index + 1, right, k_smallest)

    def partition(left, right, pivot_index):
        """Partitioning elements around the chosen pivot."""
        pivot_value = nums[pivot_index]
        # Temporarily moving pivot to the end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        store_index = left

        # Moving elements smaller than pivot to the left
        for i in range(left, right):
            if nums[i] < pivot_value:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        
        # Finally moving pivot to its correct sorted position
        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index
    
    # Adjusting k (turning 1-index into 0-index)
    return quickselect(0, len(nums) - 1, k - 1)

# Example

if __name__ == "__main__":
    data = [7, 10, 4, 3, 20, 15, 4, 7]
    k = 4

    print(f"Array: {data}")
    print(f"{k}-th smallest (Randomized Quickselect): {randomized_select(data, k)}")