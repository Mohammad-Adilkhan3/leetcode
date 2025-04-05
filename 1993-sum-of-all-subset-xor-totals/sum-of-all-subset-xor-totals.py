class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(index, current_xor):
            nonlocal total
            if index == len(nums):
                total += current_xor
                return
            dfs(index + 1, current_xor ^ nums[index])
            dfs(index + 1, current_xor)
        
        total = 0
        dfs(0, 0)
        return total