class Solution:
    def minimumSum(self, num: int) -> int:
        l=sorted(str(num))
        return int(l[0]+l[-1])+int(l[1]+l[-2])