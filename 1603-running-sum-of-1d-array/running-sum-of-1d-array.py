class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        t=0
        res=[]
        for i in nums:
            t+=i
            res.append(t)
        return res
