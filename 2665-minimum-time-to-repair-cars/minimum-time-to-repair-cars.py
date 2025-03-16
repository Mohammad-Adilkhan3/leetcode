class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right = 1, min(ranks) * cars * cars  
        while left < right:
            mid = (left + right) // 2
            total_cars = sum(int((mid // r) ** 0.5) for r in ranks) 
            if total_cars >= cars:
                right = mid  
            else:
                left = mid + 1 
        return left