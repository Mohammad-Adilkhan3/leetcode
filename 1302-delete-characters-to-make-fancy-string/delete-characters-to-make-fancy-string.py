class Solution:
    def makeFancyString(self, s: str) -> str:
        s = list(s)
        index = 1  
        for i in range(2, len(s)):
            if s[i] == s[index] and s[i] == s[index - 1]:
                continue
            index += 1
            s[index] = s[i]
        return ''.join(s[:index + 1])