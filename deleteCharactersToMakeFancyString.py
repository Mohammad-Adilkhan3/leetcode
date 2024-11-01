def make_fancy_string(s: str) -> str:
    # Convert string to a list for easier in-place modifications
    s = list(s)
    # Initialize index for the next position in the fancy string
    index = 1  # Start from the second character
    
    # Iterate from the second character to the end
    for i in range(2, len(s)):
        # If the current character and the previous two characters are the same, skip it
        if s[i] == s[index] and s[i] == s[index - 1]:
            continue
        # Otherwise, increment index and set s[index] to the current character
        index += 1
        s[index] = s[i]
    
    # Slice up to index+1 to get the final result without excess elements
    return ''.join(s[:index + 1])
