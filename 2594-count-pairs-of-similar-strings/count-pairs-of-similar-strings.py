class Solution:
    def similarPairs(self, words: List[str]) -> int:
        li=[set(i) for i in words]
        count=0
        for i in range(len(li)):
            for j in range(len(li)):
                if i < j and li[i]==li[j]:
                    count=count+1
        return (count)