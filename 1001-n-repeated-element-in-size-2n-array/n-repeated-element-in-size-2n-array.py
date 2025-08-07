class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n=len(nums)//2
        from collections import Counter
        X=Counter(nums)
        for i in X:
            if X[i]>1:
                return i
        