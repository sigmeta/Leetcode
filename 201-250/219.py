class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        se=set()
        for i in range(len(nums)):
            if nums[i] in se:
                return True
            se.add(nums[i])
            if i>=k:
                se.remove(nums[i-k])
        return False
