class Solution:
    def triangleType(self, l: List[int]) -> str:
        if l[0] + l[1] <= l[2] or l[0] + l[2] <= l[1] or l[1] + l[2] <= l[0]:return "none"
        s=len(set(l))
        if s==1:return "equilateral"
        elif s==2:return "isosceles"
        else: return "scalene"
        