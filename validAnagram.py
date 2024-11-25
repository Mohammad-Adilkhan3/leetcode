class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lis = set(s)
        for i in lis:
            if s.count(i) != t.count(i):
                return False
        return True
#one line code:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
