class Solution:
    def alternateDigitSum(self, n: int) -> int:
        l,res=len(str(n)),0
        if l%2==0: s=-1
        else: s=1
        while n>0:
            res+=(n%10)*s
            n//=10
            s*=-1
        return res

        