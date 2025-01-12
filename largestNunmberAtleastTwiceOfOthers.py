class Solution:
    def dominantIndex(self, new: List[int]) -> int:
        nums = new[:]
        nums.sort()

        if(nums[-1] >= 2 * nums[-2]):
            return new.index(nums[-1])
        else:
            return -1
