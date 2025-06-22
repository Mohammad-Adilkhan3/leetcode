class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        d,r=divmod(len(s),k)
        res=[]
        for i in range(0,d*k,k):
            res.append(s[i:i+k])
        if r>0:
            res.append((s[-r:]+((k-r)*fill)))
        return res