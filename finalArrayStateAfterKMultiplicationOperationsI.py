class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            idx = nums.index(min(nums))
            nums[idx] *= multiplier
        return nums
            #using Heap
import heapq

def modifyArray(nums, k, multiplier):
    # Create a heap with (value, index) to maintain the first occurrence order
    heap = [(val, idx) for idx, val in enumerate(nums)]
    heapq.heapify(heap)  # Turn it into a min-heap
    
    # Perform k operations
    for _ in range(k):
        # Pop the smallest element
        value, index = heapq.heappop(heap)
        # Multiply it by the multiplier
        value *= multiplier
        # Push the updated value back with its original index
        heapq.heappush(heap, (value, index))
    
    # Rebuild the final array
    result = [0] * len(nums)
    while heap:
        value, index = heapq.heappop(heap)
        result[index] = value
    
    return result
