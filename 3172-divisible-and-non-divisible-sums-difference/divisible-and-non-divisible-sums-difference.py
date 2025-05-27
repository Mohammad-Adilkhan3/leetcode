class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num2,temp=0,0
        while temp+m<=n:
            temp+=m
            num2+=temp
        t = (n*(n+1)) // 2
        return (t-num2)-num2