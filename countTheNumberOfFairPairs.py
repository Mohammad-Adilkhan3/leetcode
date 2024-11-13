from bisect import bisect_left, bisect_right

def countFairPairs(nums, lower, upper):
    # Sort the array to make binary search possible
    nums.sort()
    n = len(nums)
    fair_pairs = 0

    # Iterate over each element and find valid pairs using binary search
    for i in range(n):
        min_val = lower - nums[i]
        max_val = upper - nums[i]

        # Find the left and right bounds for nums[j]
        left_index = bisect_left(nums, min_val, i + 1, n)
        right_index = bisect_right(nums, max_val, i + 1, n)

        # Number of valid pairs with nums[i] as the first element
        fair_pairs += (right_index - left_index)

    return fair_pairs
