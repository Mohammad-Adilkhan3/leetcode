class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter
        X=Counter(chars)
        res=0
        for i in words:
            tc=X.copy()
            flag=True
            for j in i:
                if tc[j]<=0:
                    flag=False
                    break
                tc[j]-=1
            if flag:
                res+=len(i)
        return res