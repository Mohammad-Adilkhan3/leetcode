class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return False if num % 10 ==0 and num != 0 else True