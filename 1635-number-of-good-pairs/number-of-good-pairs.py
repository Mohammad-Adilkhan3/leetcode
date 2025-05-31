class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        x=Counter(nums)
        res=0
        for i in x:
            res+= x[i]*(x[i]-1)//2
        return res
