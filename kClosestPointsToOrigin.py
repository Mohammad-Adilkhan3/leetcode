class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dis(p):
            return p[0]**2 + p[1]**2
        points.sort(key=dis)
        return points[:k]
