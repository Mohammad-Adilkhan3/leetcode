class Solution:
    from collections import OrderedDict
    def minimumPushes(self, word: str) -> int:
        d=sorted(Counter(word).values(),reverse=True)
        return(sum(d[:8])+2*sum(d[8:16])+3*sum(d[16:24])+4*sum(d[24:]))