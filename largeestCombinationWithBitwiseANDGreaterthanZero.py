def largestCombination(candidates):
    # Initialize an array to store the bit count (up to 24 bits to cover the range of 10^7)
    bit_count = [0] * 24

    # Count how many numbers have each bit set
    for num in candidates:
        for i in range(24):
            if num & (1 << i):  # Check if the ith bit is set
                bit_count[i] += 1

    # The answer is the maximum count of numbers sharing a common bit
    return max(bit_count)
