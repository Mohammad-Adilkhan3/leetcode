class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        cnt = set()
        for num in arr:
            if num*2 in cnt:
                return True
            if num%2==0 and num/2 in cnt:
                return True
            cnt.add(num)
        return False
        
