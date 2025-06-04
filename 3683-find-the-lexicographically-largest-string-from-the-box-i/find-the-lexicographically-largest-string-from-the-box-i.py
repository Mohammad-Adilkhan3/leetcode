class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1 :
            return word 
        
        n = len(word)
        m = n-numFriends+1
        res = ""
            
        for i in range(0,n):
            res = max(res,word[i:m+i])

        return res 