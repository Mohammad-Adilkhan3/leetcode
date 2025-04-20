class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c=Counter(answers)
        return sum((x + 1) * ((freq + x) // (x + 1)) for x, freq in c.items())