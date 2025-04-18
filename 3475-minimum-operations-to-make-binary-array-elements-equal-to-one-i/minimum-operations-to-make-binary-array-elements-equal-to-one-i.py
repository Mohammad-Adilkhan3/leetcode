class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        operations = 0
        for i in range(n - 2):
            if nums[i] == 0:  # Found a 0, we must flip it
                operations += 1
                nums[i] ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
        return operations if nums[-2] == 1 and nums[-1] == 1 else -1


        