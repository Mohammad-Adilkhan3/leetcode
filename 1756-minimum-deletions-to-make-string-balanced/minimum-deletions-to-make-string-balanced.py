class Solution:
    def minimumDeletions(self, s: str) -> int:
        return s.count('b')-reduce(lambda q,c:max(0,q+1-2*(c<'b')),s,0)