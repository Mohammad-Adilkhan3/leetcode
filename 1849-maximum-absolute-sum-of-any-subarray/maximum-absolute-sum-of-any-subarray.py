class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        m,M,currm,currM=0,0,0,0
        for i in nums:
            currm=min(i,currm+i)
            currM=max(i,currM+i)
            m=min(m,currm)
            M=max(M,currM)
        return max(M,abs(m))
