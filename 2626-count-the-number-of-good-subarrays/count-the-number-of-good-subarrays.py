class Solution:
    from collections import defaultdict
    def countGood(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        pairs = 0
        res = 0

        for right in range(len(nums)):
            val = nums[right]
            # Add count of pairs contributed by this num
            pairs += freq[val]
            freq[val] += 1

            # Shrink window until we have less than k pairs
            while pairs >= k:
                res += len(nums) - right  # all subarrays from left to end are valid
                freq[nums[left]] -= 1
                pairs -= freq[nums[left]]  # adjust pairs after removing nums[left]
                left += 1

        return res
        