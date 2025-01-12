To solve the problem of finding two indices in an array `nums` such that the corresponding elements add up to a given `target`, we can use a hash map (dictionary) to store the elements we have seen so far and their indices. This allows us to check in constant time whether the complement (i.e., `target - current_element`) exists in the array.

Here is the Python code that implements this solution:

```python
def twoSum(nums, target):
    # Create a dictionary to store the value and its index
    num_to_index = {}
    
    # Iterate through the list
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_to_index:
            # If it exists, return the indices
            return [num_to_index[complement], i]
        
        # Otherwise, store the current number and its index in the dictionary
        num_to_index[num] = i
    
    # Since the problem guarantees one solution, this return is just a placeholder
    return []

# Example usage:
nums1 = [2, 7, 11, 15]
target1 = 9
print(twoSum(nums1, target1))  # Output: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print(twoSum(nums2, target2))  # Output: [1, 2]

nums3 = [3, 3]
target3 = 6
print(twoSum(nums3, target3))  # Output: [0, 1]
```

### Explanation:
1. **Initialization**: We start by creating an empty dictionary `num_to_index` to store the numbers we have seen so far along with their indices.
2. **Iteration**: We iterate through the list `nums` using `enumerate` to get both the index `i` and the value `num`.
3. **Complement Calculation**: For each `num`, we calculate its complement with respect to the `target` (i.e., `complement = target - num`).
4. **Check for Complement**: We check if this `complement` exists in the dictionary. If it does, it means we have found the two numbers that add up to the `target`, so we return their indices.
5. **Store Current Number**: If the complement is not found, we store the current number and its index in the dictionary and continue to the next number.
6. **Return**: Since the problem guarantees that there is exactly one solution, we will always find the indices before the loop ends.

This solution has a time complexity of O(n) and a space complexity of O(n), where n is the number of elements in the array `nums`. This is efficient and meets the problem's constraints.