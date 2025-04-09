class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(x < k for x in nums):
            return -1

        ops = 0
        seen = set()
        for x in sorted(set(nums), reverse=True):
            if x > k and x not in seen:
                seen.add(x)
                ops += 1
        return ops