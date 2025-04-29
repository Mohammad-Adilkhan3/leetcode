class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        from collections import defaultdict

        n = len(nums)
        res = 0
        left = 0
        count_max = 0
        max_val = max(nums)
        
        for right in range(n):
            if nums[right] == max_val:
                count_max += 1
            
            # Shrink the window from the left while count_max >= k
            while count_max >= k:
                if nums[left] == max_val:
                    count_max -= 1
                left += 1
            
            # All subarrays ending at right and starting from 0 to left-1 are valid
            res += left

        return res