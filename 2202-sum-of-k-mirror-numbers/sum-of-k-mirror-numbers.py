class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_pal(x: int) -> bool:
            s, y = [], x
            while y:
                s.append(y % k)
                y //= k
            return s == s[::-1]

        res, L = [], 1
        while len(res) < n:
            half = (L + 1) // 2
            start = 10**(half-1) if half > 1 else 1
            end = 10**half
            for x in range(start, end):
                s = str(x)
                if L & 1: p = int(s + s[:-1][::-1])
                else:     p = int(s + s[::-1])
                if is_pal(p):
                    res.append(p)
                    if len(res) == n:
                        return sum(res)
            L += 1

        return sum(res)