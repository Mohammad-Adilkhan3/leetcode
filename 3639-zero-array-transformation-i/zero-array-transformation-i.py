class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)  # One extra for easier range subtraction
        for l, r in queries:
            diff[l] += 1
            if r + 1 < n:
                diff[r + 1] -= 1
        decrement_count = [0] * n
        curr = 0
        for i in range(n):
            curr += diff[i]
            decrement_count[i] = curr
        for i in range(n):
            if nums[i] > decrement_count[i]:
                return False

        return True