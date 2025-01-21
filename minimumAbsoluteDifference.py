class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        m = math.inf
        arr.sort()
        res = []
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            if diff < m:
                m = diff
                res = [[arr[i], arr[i+1]]]
            elif diff == m:
                res.append([arr[i], arr[i+1]])
        return res
