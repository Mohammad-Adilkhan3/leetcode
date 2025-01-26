class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        cnt=0
        for i in range(len(nums)-1):
            if (sum(nums[:i])-sum(nums[i:]))%2==0:
                cnt+=1
        return cnt

        
