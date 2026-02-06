class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort()
        res=0
        if n==1:return res
        i=0
        for j in range(n):
            while nums[j]> nums[i]*k:
                i+=1
            res=max(res,j-i+1)
        return n-res