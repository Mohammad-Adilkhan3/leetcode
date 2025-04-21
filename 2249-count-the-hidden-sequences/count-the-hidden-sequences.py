class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        total = 0
        min_val = max_val = 0
        
        for diff in differences:
            total += diff
            min_val = min(min_val, total)
            max_val = max(max_val, total)
        
        return max(0, (upper - lower) - (max_val - min_val) + 1)