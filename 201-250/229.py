class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums)<2:
            return nums
        res=[]
        a=b=0
        cnta=cntb=0
        for n in nums:
            if n==a:
                cnta+=1
            elif n==b:
                cntb+=1
            elif cnta==0:
                a=n
                cnta=1
            elif cntb==0:
                b=n
                cntb=1
            else:
                cnta-=1
                cntb-=1
        cnta=cntb=0
        for n in nums:
            if n==a:
                cnta+=1
            elif n==b:
                cntb+=1
        if cnta>len(nums)/3:
            res.append(a)
        if a!=b and cntb>len(nums)/3:
            res.append(b)
        return res
