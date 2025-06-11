class Solution:
    def countDigits(self, num: int) -> int:
        res=0
        temp=num
        while(num>0):
            d=num%10
            if temp%d==0:
                res+=1
            num//=10
        return res