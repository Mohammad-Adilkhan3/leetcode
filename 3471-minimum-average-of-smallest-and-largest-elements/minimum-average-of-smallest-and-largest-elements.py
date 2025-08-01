class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        res=[]
        nums.sort()
        for i in range(len(nums)//2):
            res.append((nums[i]+nums[-(i+1)])/2)
        return min(res)

        