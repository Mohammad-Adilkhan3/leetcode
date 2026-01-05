class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        total_sum = 0
        negative_count = 0
        min_abs_val = float('inf')
        for i in range(n):
            for j in range(n):
                val = matrix[i][j]
                total_sum += abs(val)
                if val < 0:
                    negative_count += 1
                min_abs_val = min(min_abs_val, abs(val))
        if negative_count % 2 == 0:
            return total_sum
        else:
            return total_sum - 2 * min_abs_val