class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = set()
        n = len(nums)
        for pos,val in enumerate(nums):
            if val == key:
                left,right = pos-k, pos+k+1
                if left < 0:
                    left = 0
                if right > n:
                    right = n
                for x in range(left, right):
                    res.add(x)
        return sorted(list(res))