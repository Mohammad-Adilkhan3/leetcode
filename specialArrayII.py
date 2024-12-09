class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        # Step 1: Precompute the violations array
        violations = [0] * n
        for i in range(1, n):
            violations[i] = violations[i - 1] + (nums[i] % 2 == nums[i - 1] % 2)
        # Step 2: Process queries
        result = []
        for frm, to in queries:
            if frm == to:  # Single-element subarray is always special
                result.append(True)
            else:
                # Count violations in the range [frm+1, to]
                violationsCount = violations[to] - violations[frm]
                result.append(violationsCount == 0)
        return result
        
