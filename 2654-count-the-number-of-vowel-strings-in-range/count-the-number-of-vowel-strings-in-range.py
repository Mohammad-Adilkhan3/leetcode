class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        i=left
        res=0
        s="aeiou"
        while i<=right:
            if (words[i][0] in s ) and (words[i][-1] in s ): res+=1
            i+=1
        return res
        


        