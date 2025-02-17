class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        count = 0

        if nums[-1] < 1:
            return -1

        for i in range(len(nums)-1, -1, -1):
            count += 1

            if count <= nums[i] and (i == 0 or (count > nums[i-1])):
                return count


        return -1
        
