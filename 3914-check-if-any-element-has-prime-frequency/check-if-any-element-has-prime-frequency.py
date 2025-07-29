class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        from collections import Counter
        
        import math
        def is_prime(n):
            for i in range(2,int(math.sqrt(n))+1):
                if (n%i) == 0:
                    return False
            return True
        X=Counter(nums)
        for i in X:
            if is_prime(X[i]) and X[i]!=1:
                return True
        return False