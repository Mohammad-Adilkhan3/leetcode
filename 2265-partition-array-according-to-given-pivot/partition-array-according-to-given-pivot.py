class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l=[]
        s=[]
        g=[]
        for i in nums:
            if i<pivot:
                l.append(i)
            elif i==pivot:
                s.append(i)
            else:
                g.append(i)
        return l+s+g
        