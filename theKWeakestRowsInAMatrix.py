class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [s[1] for s in sorted([(sum(v), i) for i, v in enumerate(mat)])[:k]]
