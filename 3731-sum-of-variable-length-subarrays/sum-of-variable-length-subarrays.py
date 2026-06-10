class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] + nums[i])
        res = 0
        for j in range(len(nums)):
            i = max(0, j - nums[j])
            res += prefix[j] - (prefix[i - 1] if i > 0 else 0)
        return res