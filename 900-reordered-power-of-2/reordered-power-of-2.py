class Solution:
    def checker(self,n,v) :
        map1 = defaultdict(int)
        map2 = defaultdict(int)
        p1 = n 
        p2 = v 
        while (p1 > 0) :
            rem = p1 % 10 
            map1[rem] += 1
            p1 = p1 // 10

        while (p2 > 0) :
            rem = p2 % 10 
            map2[rem] += 1
            p2 = p2 // 10
        
        if map1 == map2 :
            return True
        
        return False
    def reorderedPowerOf2(self, n: int) -> bool:
        l = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,
             1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,
             536870912]
            
        
        if n in l :
            return True 
        
        l1 = len(str(n))

        for i in l :
            if len(str(i)) == l1 :
                check = self.checker(i,n)
                if check :
                    return True 
        
        return False 
        