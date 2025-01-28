class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0])
        for i in range(1, len(nums)):
            res &= set(nums[i])
        res = list(res)
        res.sort()
        return res
#linear code:
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        return sorted([k for k,v in Counter([x for l in nums for x in l]).items() if v==len(nums)])
