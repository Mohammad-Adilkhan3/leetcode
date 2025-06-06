class Solution:
    def robotWithString(self, s: str) -> str:
        freq = Counter(s)
        t = []
        result = []
        min_char = 'a'

        for c in s:
            t.append(c)
            freq[c] -= 1
            # Update the current minimum character still in s
            while min_char <= 'z' and freq[min_char] == 0:
                min_char = chr(ord(min_char) + 1)

            # While the top of t is <= the minimum remaining char in s, pop it
            while t and t[-1] <= min_char:
                result.append(t.pop())

        # Pop any remaining characters in t
        while t:
            result.append(t.pop())

        return ''.join(result)