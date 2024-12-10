def longestSpecialSubstring(s):
    from collections import Counter

    n = len(s)
    freq = Counter()
    
    # Generate all special substrings
    for i in range(n):
        char = s[i]
        for j in range(i, n):
            if s[j] != char:  # Break if the substring is no longer special
                break
            freq[s[i:j+1]] += 1  # Add substring to the counter
    
    # Find the longest special substring that occurs at least 3 times
    max_length = -1
    for substring, count in freq.items():
        if count >= 3:
            max_length = max(max_length, len(substring))
    
    return max_length
