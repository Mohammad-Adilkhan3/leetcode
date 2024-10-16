class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
    
        while True:
            # Sort characters by their remaining counts
            counts = [(a, 'a'), (b, 'b'), (c, 'c')]
            counts.sort(reverse=True, key=lambda x: x[0])
            for count, char in counts:
                if count > 0 and (len(result) < 2 or result[-1] != char or result[-2] != char):
                    result.append(char)
                    if char == 'a':
                        a -= 1
                    elif char == 'b':
                        b -= 1
                    elif char == 'c':
                        c -= 1
                    break
            else:
                break
        return ''.join(result)
