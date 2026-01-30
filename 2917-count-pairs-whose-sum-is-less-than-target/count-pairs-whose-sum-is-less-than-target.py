class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        res,n=0,len(nums)
        nums.sort()
        i,j=0,n-1
        while i <j:
            if nums[i]+nums[j]<target:
                res+=j-i
                i+=1
            else:
                j-=1
        return res
            
