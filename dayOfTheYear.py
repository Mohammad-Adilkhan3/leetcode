class Solution:
    def dayOfYear(self, date: str) -> int:
        res=0
        y=int(date[:4])
        if((y%4==0 and y%100!=0) or y%400==0 )and int(date[5:7])>2  :
            res+=1
        m=[31,28,31,30,31,30,31,31,30,31,30,31]
        M=int(date[5:7])
        res+=sum(m[:M-1])
        
        return res+int(date[8:])


        
