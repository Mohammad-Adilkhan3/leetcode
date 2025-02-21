class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        if num<0:
            num+=2**32
        res=hex(num)[2:]
        return res