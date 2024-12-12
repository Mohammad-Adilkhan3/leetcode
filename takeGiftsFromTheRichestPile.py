import heapq
import math

def pickGifts(gifts, k):
    # Convert gifts array into a max-heap (using negative values)
    max_heap = [-gift for gift in gifts]
    heapq.heapify(max_heap)
    
    # Perform k operations
    for _ in range(k):
        # Get the largest pile
        max_gift = -heapq.heappop(max_heap)
        # Calculate the remaining gifts
        remaining_gifts = math.floor(math.sqrt(max_gift))
        # Push the remaining gifts back into the heap
        heapq.heappush(max_heap, -remaining_gifts)
    
    # Calculate the total remaining gifts
    return -sum(max_heap)
