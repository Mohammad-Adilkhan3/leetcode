class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        C=Counter(nums)
        return  max([c for c in C if not c%2], key = lambda x:(C[x], -x), default = -1)