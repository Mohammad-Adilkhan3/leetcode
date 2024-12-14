from collections import deque

def continuousSubarrays(nums):
    n = len(nums)
    left = 0
    result = 0
    minDeque = deque()  # To maintain indices of elements in increasing order
    maxDeque = deque()  # To maintain indices of elements in decreasing order

    for right in range(n):
        # Maintain minDeque for the minimum element in the window
        while minDeque and nums[minDeque[-1]] > nums[right]:
            minDeque.pop()
        minDeque.append(right)

        # Maintain maxDeque for the maximum element in the window
        while maxDeque and nums[maxDeque[-1]] < nums[right]:
            maxDeque.pop()
        maxDeque.append(right)

        # Ensure the window is valid
        while nums[maxDeque[0]] - nums[minDeque[0]] > 2:
            # Shrink the window from the left
            if minDeque[0] == left:
                minDeque.popleft()
            if maxDeque[0] == left:
                maxDeque.popleft()
            left += 1

        # Count all subarrays ending at `right`
        result += right - left + 1

    return result
