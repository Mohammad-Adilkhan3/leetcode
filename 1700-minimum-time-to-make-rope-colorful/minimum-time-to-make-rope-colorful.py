class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n=len(colors)
        i=currsum=M=0
        res=0
        while i<n:
            if i>0 and colors[i]!=colors[i-1]:
                res+=currsum-M
                currsum=0
                M=0
            currsum+=neededTime[i]
            M=max(M,neededTime[i])
            i+=1
        res+=currsum-M

        return res

                
