class Solution:
    def numSquares(self, n: int) -> int:
        q=[[n,0]]
        se=set([n])
        dep=0
        n=0
        while n<len(q):
            k,v=q[n]
            for i in range(1,int(k**0.5)+1):
                if k-i**2==0:
                    return v+1
                elif k-i**2 in se:
                    continue
                else:
                    q.append([k-i**2,v+1])
                    se.add(k-i**2)
            n+=1
