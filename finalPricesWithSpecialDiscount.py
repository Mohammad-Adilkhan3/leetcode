def finalPrices(prices):
    n = len(prices)
    stack = []
    result = prices[:]

    for i in range(n):
        # Check the stack for discounts
        while stack and prices[stack[-1]] >= prices[i]:
            idx = stack.pop()
            result[idx] -= prices[i]
        stack.append(i)

    return result
