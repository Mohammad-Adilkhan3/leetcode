class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc=Counter(ransomNote) 
        mc=Counter(magazine)
        for i in rc:
            if rc[i]>mc[i]:
                return False
        return True
