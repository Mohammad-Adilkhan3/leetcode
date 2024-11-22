def maxEqualRowsAfterFlips(matrix):
    from collections import defaultdict

    pattern_count = defaultdict(int)

    for row in matrix:
        # Normalize the row: if the first element is 1, flip the entire row
        normalized = tuple(cell ^ row[0] for cell in row)
        pattern_count[normalized] += 1

    # The maximum value in the hash map is the result
    return max(pattern_count.values())
