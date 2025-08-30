class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        counts = defaultdict(int)
        for i in range(lowLimit, highLimit +1):
            s = sum([int(x) for x in list(str(i))])
            counts[s] += 1
        return max(counts.values())