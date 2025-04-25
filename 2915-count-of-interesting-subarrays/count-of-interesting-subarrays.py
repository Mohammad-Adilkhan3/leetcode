class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count = defaultdict(int)
        count[0] = 1  
        result = 0
        prefix = 0
        for num in nums:
            if num % modulo == k:
                prefix += 1
            target = (prefix - k) % modulo
            result += count[target]
            count[prefix % modulo] += 1

        return result