class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        total_count = nums.count(candidate)
        left_count = 0
        n = len(nums)
        for i in range(n - 1):  # Ensure at least one element remains on the right
            if nums[i] == candidate:
                left_count += 1
            left_size = i + 1
            right_size = n - left_size
            right_count = total_count - left_count
            if left_count * 2 > left_size and right_count * 2 > right_size:
                return i  # Minimum index found

        return -1