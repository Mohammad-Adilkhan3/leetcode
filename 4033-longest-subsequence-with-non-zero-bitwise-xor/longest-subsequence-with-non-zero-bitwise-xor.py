class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        return  [0, len(nums) -1 +(reduce(xor,nums)!=0)][any(nums)]