class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator ==0:return "0"
        frac=[]
        if (numerator<0)^ (denominator<0):
            frac.append("-")
        dividend=abs(numerator)
        divisor=abs(denominator)
        frac.append(str(dividend//divisor))
        rem=dividend%divisor
        if rem==0:
            return "".join(frac)
        frac.append(".")
        d={}
        while rem!=0:
            if rem in d:
                frac.insert(d[rem],"(")
                frac.append(")")
                break
            d[rem]=len(frac)
            rem*=10
            frac.append(str(rem//divisor))
            rem%=divisor
        return "".join(frac)
