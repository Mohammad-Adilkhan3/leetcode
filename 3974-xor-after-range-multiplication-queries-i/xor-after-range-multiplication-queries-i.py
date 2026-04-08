class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        for l, r, k, v in queries:
            # Apply updates to indices l, l+k, l+2k, ... ≤ r
            for idx in range(l, r + 1, k):
                nums[idx] = (nums[idx] * v) % MOD
        
        # Compute XOR of all elements
        result = 0
        for x in nums:
            result ^= x
        return result