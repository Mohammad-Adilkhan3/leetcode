class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        X=Counter(nums)
        res=0
        for i in X:
            if X[i]==1:
                res+=i
        return res
        