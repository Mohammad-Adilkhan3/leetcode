class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        N = n * n
        seen = set()
        repeated = -1
        missing = -1
        for row in grid:
            for num in row:
                if num in seen:
                    repeated = num  # Found the duplicate number
                seen.add(num)
        for num in range(1, N + 1):
            if num not in seen:
                missing = num  # Found the missing number
                break
        return [repeated, missing]