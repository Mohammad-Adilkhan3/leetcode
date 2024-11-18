def decrypt(code, k):
    n = len(code)
    if k == 0:
        return [0] * n

    result = [0] * n
    direction = 1 if k > 0 else -1  # Determine direction based on k
    k = abs(k)
    
    for i in range(n):
        current_sum = 0
        for j in range(1, k + 1):
            current_sum += code[(i + direction * j) % n]
        result[i] = current_sum

    return result
