def countGoodStrings(low, high, zero, one):
    MOD = 10**9 + 7
    dp = [0] * (high + 1)
    dp[0] = 1  # Base case: one way to form an empty string
    
    for i in range(1, high + 1):
        if i - zero >= 0:
            dp[i] = (dp[i] + dp[i - zero]) % MOD
        if i - one >= 0:
            dp[i] = (dp[i] + dp[i - one]) % MOD
    
    # Sum up the counts for lengths in the range [low, high]
    return sum(dp[low:high + 1]) % MOD
