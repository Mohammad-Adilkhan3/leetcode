class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        freq = Counter(s)
    
        # Count odd-frequency characters
        odd_count = sum(1 for count in freq.values() if count % 2 != 0)
        
        # Check conditions
        return odd_count <= k <= len(s)
