class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:  # If total candies are less than children, return 0
            return 0
        low, high = 1, max(candies)
        res = 0
        while low <= high:
            mid = (low + high) // 2
            children_served = sum(c // mid for c in candies)
            if children_served >= k:  # If we can serve at least k children
                res = mid 
                low = mid + 1 
            else:
                high = mid - 1  
        return res
            