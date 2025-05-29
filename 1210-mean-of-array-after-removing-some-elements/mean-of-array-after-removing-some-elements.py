class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        p=int(len(arr)*0.05)
        return sum(arr [p:-(p)])/len(arr [p:-(p)])