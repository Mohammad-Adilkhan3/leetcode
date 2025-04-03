class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        v,d,res=0,0,0
        for i in nums:
            res=max(res,d*i)
            d=max(d,v-i)
            v=max(v,i)
        return res