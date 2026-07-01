class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        res = 0
        for x in freq:
            if freq[x]%k == 0:
                res += (x*freq[x])
        return res
 
