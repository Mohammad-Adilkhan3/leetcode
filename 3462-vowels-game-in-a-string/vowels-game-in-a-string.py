class Solution:
    def doesAliceWin(self, s: str) -> bool:
        c=Counter(s)
        v="aeiou"
        t=0
        for i in c:
            if i in v:
                t+=c[i]
        return t!=0


