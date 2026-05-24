class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n=len(arr)
        low,high=0,n-1
        while low<=high:
            mid=low+(high-low)//2
            cnt=arr[mid]-mid-1
            if cnt<k:
                low=mid+1
            else:
                high=mid-1

        return k if high<0 else high+k+1