class Solution:
    def checkStrings(self, s: str, t: str) -> bool:
        return all(Counter(s[q::2])==Counter(t[q::2]) for q in (0,1))