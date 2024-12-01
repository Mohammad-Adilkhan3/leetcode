class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[0] > nums[-1]:
            nums = nums[::-1]

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]: 
                return False

        return True
#linear code
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
      return sorted(nums)==nums or sorted(nums)==nums[::-1]
