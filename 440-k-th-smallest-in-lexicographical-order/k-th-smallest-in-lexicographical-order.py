class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(prefix, n):
            current = prefix
            next_prefix = prefix + 1
            steps = 0
            while current <= n:
                steps += min(n + 1, next_prefix) - current
                current *= 10
                next_prefix *= 10
            return steps
    
        current = 1
        k -= 1  # because we start with 1
        
        while k > 0:
            steps = count_steps(current, n)
            if k >= steps:
                k -= steps
                current += 1
            else:
                current *= 10
                k -= 1
                
        return current
        
        
