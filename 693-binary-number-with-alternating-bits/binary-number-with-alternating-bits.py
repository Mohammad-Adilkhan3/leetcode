class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b=bin(n)
        return not(("00" in b) or ("11" in b))