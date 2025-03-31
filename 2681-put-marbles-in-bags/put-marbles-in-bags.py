class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == 1:  # Only one bag means no partitioning, difference is 0
            return 0
        
        pair_sums = [weights[i] + weights[i+1] for i in range(n-1)]
        pair_sums.sort()

        # Compute min and max scores using k-1 splits
        min_score = sum(pair_sums[:k-1])
        max_score = sum(pair_sums[-(k-1):])

        return max_score - min_score