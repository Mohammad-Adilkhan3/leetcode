class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        lef=1
        for i in range (len(nums)):
            res[i]*=lef
            lef*= nums[i]
        rig=1
        for i in range (len(nums)-1,-1,-1):
            res[i]*= rig
            rig *= nums[i]
        return res
        