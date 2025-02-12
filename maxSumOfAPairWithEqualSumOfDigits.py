class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(num):
            return sum(int(digit) for digit in str(num))

        digit_map = {}  # Stores max number for each digit sum
        max_sum = -1

        for num in nums:
            d_sum = digit_sum(num)
            if d_sum in digit_map:
                max_sum = max(max_sum, num + digit_map[d_sum])
            digit_map[d_sum] = max(num, digit_map.get(d_sum, 0))

        return max_sum

        
