class Solution:
    def minBitwiseArray(self, a: List[int]) -> List[int]:
        return [v%2-1 or v-(-~v&~v)//2 for v in a]