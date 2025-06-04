class Solution:
    def arraySign(self, nums: List[int]) -> int:
        import math
        def si(x):
            if x>0:
                return 1
            elif x<0:
                return -1
            else:
                return 0
        return si(math.prod(nums))