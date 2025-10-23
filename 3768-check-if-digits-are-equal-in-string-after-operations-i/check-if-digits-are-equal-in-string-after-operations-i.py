class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            res=[]
            for i in range(len(s)-1):
                res.append(str((int(s[i])+int(s[i+1]))%10))
            s="".join(res)
        return s[0]==s[1]