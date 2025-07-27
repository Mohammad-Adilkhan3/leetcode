class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res,l=0,0
        for i in range(1,len(nums)-1):
            if nums[i]!=nums[i+1]:
                if( nums[i]>nums[l] and nums[i]>nums[i+1]) or (nums[i]<nums[l] and nums[i]<nums[i+1]):
                    res+=1
                l=i
        return res
