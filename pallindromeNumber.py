class Solution:
    def isPalindrome(self, x: int) -> bool:
        X=str(x)
        return X==X[::-1]
        
