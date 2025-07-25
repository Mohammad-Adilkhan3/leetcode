class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums)<0:
            return max(nums)

        return sum({i for i in nums if i>0})
        