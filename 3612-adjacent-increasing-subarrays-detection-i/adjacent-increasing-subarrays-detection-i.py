class Solution:
    def hasIncreasingSubarrays(self, a: List[int], k: int) -> bool:
        q = [*accumulate(map(lt,a,a[1:]),lambda q,p:q*p+1,initial=1)]
        return any(q1>=k<=q2 for q1,q2 in zip(q,q[k:]))