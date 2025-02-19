class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt,res=0,0
        for i in s:
            if i=="L":
                cnt+=1
            elif i=="R":
                cnt-=1
            if cnt==0:
                res+=1
        return res
