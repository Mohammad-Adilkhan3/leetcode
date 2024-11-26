class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s=list(set(nums))
        s.sort()
        n=len(s)
        if n<3:
            return s[n-1]
        return s[-3]
