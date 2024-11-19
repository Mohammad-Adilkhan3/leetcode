def maximumSubarraySum(nums, k):
    n = len(nums)
    max_sum = 0
    current_sum = 0
    start = 0
    seen = set()

    for end in range(n):
        # Add the current element
        while nums[end] in seen:
            seen.remove(nums[start])
            current_sum -= nums[start]
            start += 1

        seen.add(nums[end])
        current_sum += nums[end]

        # Check if we have a valid subarray of size k
        if end - start + 1 == k:
            max_sum = max(max_sum, current_sum)

            # Slide the window
            seen.remove(nums[start])
            current_sum -= nums[start]
            start += 1

    return max_sum

# Example Usage
nums1 = [1, 5, 4, 2, 9, 9, 9]
k1 = 3
print(maximumSubarraySum(nums1, k1))  # Output: 15

nums2 = [4, 4, 4]
k2 = 3
print(maximumSubarraySum(nums2, k2))  # Output: 0
