class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        t=sorted(heights)
        res=0
        for i in range(len(heights)):
            if t[i]!=heights[i]:
                res+=1
        return res
        