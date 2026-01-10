class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        d=dict()
        for i in range(len(order)):
            if order[i] not in d:
                d[order[i]]=i
        friends.sort(key=lambda x:(d.get(x,float('inf')),x))
        return friends