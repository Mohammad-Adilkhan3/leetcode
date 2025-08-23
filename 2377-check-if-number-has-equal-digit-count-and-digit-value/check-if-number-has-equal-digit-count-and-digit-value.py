class Solution:
    def digitCount(self, num: str) -> bool:
        C=Counter(num)
        for i in range(len(num)):
            if int(num[i])!=C[str(i)]: return False
        return True
        