class Solution:
    def judgeCircle(self, s: str) -> bool:
        return sum(map({'L':-1,'R':1,'U':1j,'D':-1j}.get,s))==0