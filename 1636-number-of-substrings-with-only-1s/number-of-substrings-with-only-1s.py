class Solution:
    def numSub(self, s: str) -> int:
        curr,res=0,0
        M=10**9+7
        for i in s:
            if i=='1':
                curr=(curr+1)%M
            else:
                curr=0
            res=(res+curr)%M
        return res
    