def findRelativeRanks(self, score: List[int]) -> List[str]:
        sc = sorted(score,reverse=True)
        o={}
        for i in range(len(sc)):
            if i==0:
                o[sc[i]]="Gold Medal"
            elif i==1:
                o[sc[i]]="Silver Medal"
            elif i==2:
                o[sc[i]]="Bronze Medal"
            else:
                o[sc[i]]= str(i+1)
        res=[]
        for i in score:
            res.append(o[i])
        return res
