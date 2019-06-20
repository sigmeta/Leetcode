class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res=[]
        tag=True
        s=nums[0]
        for i in range(len(nums)):
            if tag:
                s=nums[i]
                tag=False
            e=nums[i]
            if i==len(nums)-1 or nums[i+1]-nums[i]>1:
                if e>s:
                    res.append(str(s)+'->'+str(e))
                else:
                    res.append(str(e))
                tag=True
        return res
