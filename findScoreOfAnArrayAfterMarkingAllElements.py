class Solution:
    def findScore(self, nums: List[int]) -> int:
        
        ans = 0
        vis = [False] * (len(nums)+2)

        for i,x in sorted(enumerate(nums,1), key = lambda p :p[1]):
            if not vis[i]:
                vis[i-1] = vis[i+1] = True
                ans+=x
        return ans
