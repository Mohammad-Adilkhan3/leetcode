class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        x=Counter(words)
        res=sorted(x.keys(), key=lambda i: (-x[i],i))
        return res[:k]

        