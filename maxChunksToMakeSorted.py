def maxChunksToSorted(arr):
    max_so_far = 0
    chunks = 0
    
    for i in range(len(arr)):
        max_so_far = max(max_so_far, arr[i])
        if max_so_far == i:
            chunks += 1
    
    return chunks

# Example Usage
print(maxChunksToSorted([4, 3, 2, 1, 0]))  # Output: 1
print(maxChunksToSorted([1, 0, 2, 3, 4]))  # Output: 4
