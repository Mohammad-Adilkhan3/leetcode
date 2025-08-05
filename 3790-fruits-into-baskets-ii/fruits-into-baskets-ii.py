class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n=len(fruits)
        i,j=0,0
        cnt=0
        while i<n:
            j = 0
            while j<n:
                if fruits[i]<=baskets[j] :
                    baskets[j]=0
                    cnt+=1
                    break
                j+=1
            i+=1
        return n-cnt

