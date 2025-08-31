class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count=0
        mydict=Counter(nums)   
        for i in mydict:
            if i+k in mydict:
                count=count+ mydict[i]*mydict[i+k]  
        return count