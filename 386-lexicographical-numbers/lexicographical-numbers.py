class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        s,res=[],[]
        for i in range(1,n+1):
            s.append(str(i))
        s.sort()
        for i in s:
            res.append(int(i))
        return res
