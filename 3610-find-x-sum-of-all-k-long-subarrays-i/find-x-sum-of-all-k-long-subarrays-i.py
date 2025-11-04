class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
        n=len(nums)
        res=[]
        for i in range(n-k+1):
            C=Counter(nums[i:i+k])
            if len(C)<=x:
                res.append(sum(nums[i:i+k]))
                continue
            S=sorted(C.items(), key=lambda x:(-x[1],-x[0]))
            print(S)
            j=0
            su=0
            for m,n in S:
                if j==x:
                    break
                su+= m * n
                j+=1
            res.append(su)
        return res


            
                
