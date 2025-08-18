class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        res=0
        c1=Counter(words1)
        c2=Counter(words2)
        for i in c1:
            if i in c2 and c1[i]==1 and c2[i]==1:
                res+=1
        return res
        