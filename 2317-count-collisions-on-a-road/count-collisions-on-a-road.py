class Solution(object):
    def countCollisions(self, s):
        """
        :type directions: str
        :rtype: int
        """
        return len(s.lstrip('L').rstrip('R').replace('S',''))