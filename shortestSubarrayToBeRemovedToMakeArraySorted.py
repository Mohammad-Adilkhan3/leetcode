def shortestSubarrayToRemove(arr):
    n = len(arr)
    
    # Step 1: Find the longest non-decreasing prefix
    left = 0
    while left < n - 1 and arr[left] <= arr[left + 1]:
        left += 1
    
    # If the array is already non-decreasing
    if left == n - 1:
        return 0
    
    # Step 2: Find the longest non-decreasing suffix
    right = n - 1
    while right > 0 and arr[right - 1] <= arr[right]:
        right -= 1
    
    # Step 3: Calculate the minimum subarray to remove
    result = min(n - left - 1, right)  # Remove prefix or suffix
    
    # Step 4: Merge prefix and suffix using two pointers
    i, j = 0, right
    while i <= left and j < n:
        if arr[i] <= arr[j]:
            result = min(result, j - i - 1)
            i += 1
        else:
            j += 1
    
    return result

# Example Usage
print(shortestSubarrayToRemove([1, 2, 3, 10, 4, 2, 3, 5]))  # Output: 3
print(shortestSubarrayToRemove([5, 4, 3, 2, 1]))           # Output: 4
print(shortestSubarrayToRemove([1, 2, 3]))                 # Output: 0
