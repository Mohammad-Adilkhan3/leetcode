class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(0,len(nums)-2,3):
            arr=(nums[i:i+3])
            if k< arr[-1] - arr[0]:
                return []
            res.append(arr)
        return res
        

        