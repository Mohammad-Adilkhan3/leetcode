class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c=[]
        for i in set(nums):
            c.append(nums.count(i))
        return (max(c)*c.count(max(c)))