class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ctr=0
        result=str()
        for i in s:
            if i=='(':
                if ctr==0:
                    ctr+=1
                else:
                    result+=i
                    ctr+=1
            else:
                if ctr==1:
                    ctr-=1
                else:
                    result+=i
                    ctr-=1
        return result