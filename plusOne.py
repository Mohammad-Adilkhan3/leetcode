 def plusOne(self, digits: List[int]) -> List[int]:
        n=int("".join(map(str,digits)))+1
        res=list(map(int,str(n)))
        return res
