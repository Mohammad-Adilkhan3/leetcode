class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res , i , j = set() , 0 , 0
        tempx , tempy= x**i , y**j
        while tempx<bound:
            while tempx + tempy <= bound:
                res.add(tempx+tempy)
                j+=1
                tempy = y**j
                if y==1:  break
            i+=1
            tempx = x**i
            j = 0
            tempy = y**j
            if x==1: break
        return list(res)
