class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        now,length=0,0
        minlen=len(nums)+1
        for i,n in enumerate(nums):
            if now+n<s:
                now+=n
                length+=1
            else:
                now+=n
                length+=1
                while now>=s:
                    now-=nums[i-length+1]
                    minlen=min(minlen,length)
                    length-=1
        if minlen>len(nums):
            return 0
        else:
            return minlen
                
