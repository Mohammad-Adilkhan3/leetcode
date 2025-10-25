class Solution:
    def totalMoney(self, n: int) -> int:
        d,m=divmod(n,7)
        return (d*(49+7*d)+ m*(2*d+m+1))//2