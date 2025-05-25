class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        result = 0
        central = False  # To track if we can place one self-palindrome in the center

        for word in list(count.keys()):
            rev = word[::-1]
            if word != rev:
                pair = min(count[word], count[rev])
                result += pair * 4  # Each pair contributes 4 to the length
                count[word] -= pair
                count[rev] -= pair
            else:
                pair = count[word] // 2
                result += pair * 4
                count[word] -= pair * 2
                if count[word] > 0:
                    central = True

        if central:
            result += 2  # Add one self-palindrome in the center

        return result


        