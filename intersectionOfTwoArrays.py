class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1=Counter(nums1)
        res=[]
        for i in nums2:
            if n1[i]>0:
                res.append(i)
                n1[i]-=1
        return res
