class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        i=1
        n=len(height)
        res=[]
        while i<n:
            if height[i]!=0 and height[i-1]>threshold:
                res.append(i)
            i+=1
        return res

