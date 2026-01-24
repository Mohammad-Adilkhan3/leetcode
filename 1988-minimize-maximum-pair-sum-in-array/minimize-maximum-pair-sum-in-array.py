class Solution:
    def minPairSum(self, n: List[int]) -> int:
        return max(map(add, s:=sorted(n), s[::-1]))