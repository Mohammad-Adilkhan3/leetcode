class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        res=[0]*n
        for i in range(n):
            res[i]=len(set(A[:i+1]).intersection(set(B[:i+1])))
        return res
