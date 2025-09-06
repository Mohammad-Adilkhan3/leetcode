class Solution:
    def maxFrequencyElements(self, a: List[int]) -> int:
        return prod(max(Counter(Counter(a).values()).items()))