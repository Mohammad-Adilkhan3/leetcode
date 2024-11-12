def maximumBeauty(items, queries):
    # Sort items by price
    items.sort()
    
    # Sort queries, but keep track of original indices
    sorted_queries = sorted((q, i) for i, q in enumerate(queries))
    
    # Initialize result array
    result = [0] * len(queries)
    
    # Initialize variables
    max_beauty = 0
    item_index = 0
    
    # Process each query in ascending order
    for query, q_index in sorted_queries:
        # Move through items within price range of the current query
        while item_index < len(items) and items[item_index][0] <= query:
            # Update the maximum beauty seen so far
            max_beauty = max(max_beauty, items[item_index][1])
            item_index += 1
        
        # The answer for this query is the max beauty up to this price
        result[q_index] = max_beauty
    
    return result

# Test examples
print(maximumBeauty([[1,2],[3,2],[2,4],[5,6],[3,5]], [1,2,3,4,5,6]))  # Expected: [2,4,5,5,6,6]
print(maximumBeauty([[1,2],[1,2],[1,3],[1,4]], [1]))                 # Expected: [4]
print(maximumBeauty([[10,1000]], [5]))                               # Expected: [0]
