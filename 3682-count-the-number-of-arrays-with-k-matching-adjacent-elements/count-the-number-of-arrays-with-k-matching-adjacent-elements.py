class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return (m * math.comb(n - 1, k) * ((m - 1) ** (n - k - 1))) % ((10 ** 9) + 7)