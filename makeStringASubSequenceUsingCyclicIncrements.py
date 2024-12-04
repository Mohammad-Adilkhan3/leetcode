class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        ans,n,m=0,len(str1),len(str2)
        for i in range(n):
            if ans < m and (ord(str2[ans]) - ord(str1[i]))%26 <= 1:
                ans+=1
        return ans == m
  #Breif Code
  def canBeSubsequence(str1, str2):
    n, m = len(str1), len(str2)
    i, j = 0, 0  # i for str1, j for str2

    while i < n and j < m:
        # Check if we can match str1[i] with str2[j]
        if str1[i] == str2[j]:
            j += 1  # move to next character in str2
        elif (ord(str1[i]) + 1 - ord('a')) % 26 == (ord(str2[j]) - ord('a')) % 26:
            # Check if one cyclic increment can match the characters
            j += 1  # move to next character in str2
        i += 1  # move to next character in str1

    # If we have matched all characters of str2
    return j == m

# Example test cases:
print(canBeSubsequence("abc", "ad"))  # Output: True
print(canBeSubsequence("zc", "ad"))  # Output: True
print(canBeSubsequence("ab", "d"))   # Output: False
