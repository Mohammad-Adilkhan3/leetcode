class Solution:
    def averageValue(self, nums: List[int]) -> int:
        res,cnt=0,0
        for i in nums:
            if i%6==0:
                res+=i
                cnt+=1
        return res//cnt if cnt>0 else 0
        