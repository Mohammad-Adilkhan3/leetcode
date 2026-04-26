class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        res=[]
        for i in candies:
            res.append(True) if i+extraCandies>=m else res.append(False)
        return res
