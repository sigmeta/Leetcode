class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2=i3=i5=0
        res=[1]
        while len(res)<n:
            res.append(min(res[i2]*2,res[i3]*3,res[i5]*5))
            if res[-1]==res[i2]*2: i2+=1
            if res[-1]==res[i3]*3:i3+=1
            if res[-1]==res[i5]*5:i5+=1
        return res[-1]
