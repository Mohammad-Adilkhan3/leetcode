class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        for i in range(n):
            o=set()
            e=set()
            for j in range(i,n):
                if nums[j]%2==0:e.add(nums[j])
                else:o.add(nums[j])
                if len(o)==len(e):res=max(res,j-i+1)
        return res