class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        total = 0
        for right in range(len(s)):
            count[s[right]] += 1
            while all(count.values()): 
                count[s[left]] -= 1
                left += 1
            total += left 
        return total
        