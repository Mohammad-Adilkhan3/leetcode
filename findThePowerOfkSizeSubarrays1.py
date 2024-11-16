class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res=[]
        n=len(nums)
        if len(nums)<k:
            res.append(-1)
        for i in range(n-k+1):
            if nums[i:i+k]==sorted(nums[i:i+k]) and len(set(nums[i:i+k]))==k and max(nums[i:i+k])-min(nums[i:i+k])==k-1:
                res.append(max(nums[i:i+k]))
            else:
                res.append(-1)
        return res
