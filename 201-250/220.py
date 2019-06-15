class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        dct={}
        for i,n in enumerate(nums):
            if t<=k:
                for j in range(n-t,n+t+1):
                    if j in dct and i-dct[j]<=k:
                        return True
            else:
                for ke,v in dct.items():
                    if abs(n-ke)<=t and i-v<=k:
                        return True
            dct[n]=i
        return False
