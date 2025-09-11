class Solution:
    def sortVowels(self, s: str) -> str:
        t=[]
        res=[]
        k,j=0,0
        v="AEIOUaeiou"
        for i in s:
            if i in v:
                t.append(i)
        t.sort()
        while k<len(s):
            if s[k] in v:
               res.append(t[j])
               j+=1
            else:
                res.append(s[k])
            k+=1
        return "".join(res)

