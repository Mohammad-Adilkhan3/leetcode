class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res=0
        for i in costs:
            if coins-i<0:
                return res
            coins-=i
            res+=1
        return res
