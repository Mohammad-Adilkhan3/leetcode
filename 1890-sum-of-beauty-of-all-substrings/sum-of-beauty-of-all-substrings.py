class Solution:
    def beautySum(self, s: str) -> int:
        from collections import Counter
        curr_sum = 0
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                d = Counter(s[i:j+1])
                if len(d) > 1:
                    diff = max(d.values()) - min(d.values())
                    curr_sum += diff

        return curr_sum