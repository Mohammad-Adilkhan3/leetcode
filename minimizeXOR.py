class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count2 = bin(num2).count('1')
        x = 0
        # Step 1: Traverse bits of num1 from MSB to LSB
        for i in range(31, -1, -1):  # 32-bit integers
            if count2 == 0:  # No more set bits needed
                break
            if num1 & (1 << i):  # If bit i in num1 is set
                x |= (1 << i)  # Set the same bit in x
                count2 -= 1
        for i in range(32):
            if count2 == 0:  # No more set bits needed
                break
            if not (x & (1 << i)):  # If bit i in x is not set
                x |= (1 << i)  # Set bit i in x
                count2 -= 1
        return x
