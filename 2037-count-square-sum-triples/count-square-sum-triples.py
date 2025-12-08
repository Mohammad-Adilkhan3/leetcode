class Solution:
    def countTriples(self, n: int) -> int:
        return sum(a*a+b*b==c*c for a,b,c in combinations(range(n+1),3))*2