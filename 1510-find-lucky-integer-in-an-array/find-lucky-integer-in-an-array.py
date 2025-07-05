class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res=-1
        x=Counter(arr)
        for i in x:
            if int(i)==x[i]:
                res=max(res,x[i])
        return res

        