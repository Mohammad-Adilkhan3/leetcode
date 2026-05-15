class Solution:
    def findMin(self, nums: List[int]) -> int:
       return nums[bisect_left(nums,True,key= lambda x: x<=nums[-1])]