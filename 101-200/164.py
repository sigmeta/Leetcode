class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return 0
        minValue = 2**32
        maxValue = -2**32
        for num in nums:
            minValue = min(minValue, num)
            maxValue = max(maxValue, num)
        
        
        bucket_range = (maxValue - minValue) // len(nums) + 1
        bucket_num = (maxValue - minValue) // bucket_range + 1
        
        hashmapMax = {}
        hashmapMin = {}
        for i in range(len(nums)):
            bucket_id = (nums[i]-minValue) // bucket_range
            if not bucket_id in hashmapMax:
                hashmapMax[bucket_id] = nums[i]
                hashmapMin[bucket_id] = nums[i]
            else:
                
                hashmapMax[bucket_id] = max(hashmapMax[bucket_id],nums[i])
                hashmapMin[bucket_id] = min(hashmapMin[bucket_id],nums[i])
            
        prev = 0
        res = 0
        
        for i in range(1,bucket_num):
            if not i in hashmapMax:
                continue
            if not prev in hashmapMax:
                continue
            res = max(res, hashmapMin[i] - hashmapMax[prev])
            prev = i
        return res
        
