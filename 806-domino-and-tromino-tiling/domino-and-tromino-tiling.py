class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        sum_dp = dp[0]  # sum of dp[0] to dp[n-3] for current n

        for i in range(3, n + 1):
            dp[i] = (2 * sum_dp + dp[i - 1] + dp[i - 2]) % MOD
            sum_dp = (sum_dp + dp[i - 2]) % MOD

        return dp[n]