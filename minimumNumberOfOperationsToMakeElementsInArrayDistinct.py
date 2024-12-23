class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt=0
        while len(nums)!=len(set(nums)):
           cnt+=1
           nums=nums[3:]
        return cnt
            
