class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        ret = deque(arr[:k])
        for r in range(k, len(arr)):
            if abs(arr[r] - x) < abs(arr[l] - x):
                l += 1
                ret.popleft()
                ret.append(arr[r])
        
        return list(ret)