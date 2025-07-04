class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s=0
        t=x
        while x>0:
            s+=x%10
            x//=10
        return s if t%s==0 else -1