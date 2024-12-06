def maxCount(banned, n, maxSum):
    banned_set = set(banned)
    current_sum = 0
    count = 0

    for num in range(1, n + 1):
        if num in banned_set:
            continue
        if current_sum + num > maxSum:
            break
        current_sum += num
        count += 1

    return count
