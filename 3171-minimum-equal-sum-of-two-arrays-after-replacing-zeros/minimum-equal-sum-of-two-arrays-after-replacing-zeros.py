class Solution:
    def minSum(self, num1: List[int], num2: List[int]) -> int:
        sum1 = sum(num1)
        sum2 = sum(num2)
        zeros1 = num1.count(0)
        zeros2 = num2.count(0)
        
        if zeros1 == 0 and zeros2 == 0:
            return sum1 if sum1 == sum2 else -1
        elif zeros1 == 0:
            return sum1 if sum2 + zeros2 <= sum1 else -1
        elif zeros2 == 0:
            return sum2 if sum1 + zeros1 <= sum2 else -1
        
        return max(sum1 + zeros1, sum2 + zeros2)