class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans=0
        for i, j in combinations(words,2):
            ans+= j.startswith(i) and j.endswith(i)

        return  ans
        
