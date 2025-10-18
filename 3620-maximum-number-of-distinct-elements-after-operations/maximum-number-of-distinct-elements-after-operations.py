class Solution:
    def maxDistinctElements(self, a: List[int], k: int) -> int:
        p = -inf
        return len({p:=max(p,min(max(v-k,p+1),v+k)) for v in sorted(a)})