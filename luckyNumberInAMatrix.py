class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        return [x] if (x:=max(min(i) for i in matrix))==min(max(j) for j in zip(*matrix)) else []
