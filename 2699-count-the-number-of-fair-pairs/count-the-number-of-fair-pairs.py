class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        from bisect import bisect_left, bisect_right
        nums.sort()
        n = len(nums)
        fair_pairs = 0
        for i in range(n):
            min_val = lower - nums[i]
            max_val = upper - nums[i]
            left_index = bisect_left(nums, min_val, i + 1, n)
            right_index = bisect_right(nums, max_val, i + 1, n)
            fair_pairs += (right_index - left_index)
        return fair_pairs