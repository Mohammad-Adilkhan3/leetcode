class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p,s=1,0
        for i in range(len(str(n))):
            r=n%10
            n//=10
            s+=r
            p*=r
        return p-s
        