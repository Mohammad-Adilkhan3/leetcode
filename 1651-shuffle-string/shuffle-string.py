class Solution:
    def restoreString(self, s: str, p: List[int]) -> str:
        return "".join([v for (i,v) in sorted(zip(p,s))])