class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        n = len(word)
        i = 0
        while i < n:
            count = 1
            while i + 1 < n and word[i] == word[i + 1] and count < 9:
                count += 1
                i += 1
            comp += str(count) + word[i]
            i += 1
        return comp
      
