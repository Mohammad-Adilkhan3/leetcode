class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = s = l = 0
        for r, x in enumerate(nums):
            s += x
            while s * (r - l + 1) >= k:
                s -= nums[l]
                l += 1
            ans += r - l + 1
        return ans