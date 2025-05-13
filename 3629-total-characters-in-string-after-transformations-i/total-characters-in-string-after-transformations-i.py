class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        from collections import Counter

        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        for _ in range(t):
            next_freq = [0] * 26
            for i in range(26):
                if i == 25:  # 'z'
                    next_freq[0] = (next_freq[0] + freq[i]) % MOD  # 'a'
                    next_freq[1] = (next_freq[1] + freq[i]) % MOD  # 'b'
                else:
                    next_freq[i+1] = (next_freq[i+1] + freq[i]) % MOD
            freq = next_freq

        return sum(freq) % MOD