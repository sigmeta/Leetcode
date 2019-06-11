class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)<3:
            return max(nums)
        f,s=0,0
        for n in nums[:-1]:
            f,s=s,max(f+n,s)
        res=s
        f,s=0,0
        for n in nums[1:]:
            f,s=s,max(f+n,s)
        return max(res,s)
