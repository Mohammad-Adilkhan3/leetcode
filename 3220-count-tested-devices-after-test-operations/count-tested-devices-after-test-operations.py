class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        cnt=0
        for i in range(len(batteryPercentages)):
            batteryPercentages[i]-=cnt
            if batteryPercentages[i]>0:
                cnt+=1
        return cnt
            