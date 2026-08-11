class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_sum = nums[0]
        storage = set(nums)

        index = 1

        # Find the sum of the longest consecutive prefix
        while index < len(nums) and nums[index] == nums[index - 1] + 1:
            prefix_sum += nums[index]
            index += 1

        # Find the smallest missing integer
        while prefix_sum in storage:
            prefix_sum += 1

        return prefix_sum