class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        mod = 10**9 + 7
        y_count = Counter(p[1] for p in points)
        total = 0
        sqr_sum = 0
        for cnt in y_count.values():
            sides = cnt * (cnt - 1) // 2
            total += sides
            sqr_sum += sides * sides
        res = (total * total - sqr_sum) // 2
        return res % mod

        