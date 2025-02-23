class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0: return '0'
        res,n="",abs(num)
        while n:
            n,m=divmod(n,7)
            res+=str(m)
        if num<0: res+="-"
        return res[::-1]