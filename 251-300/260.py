class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        se=set()
        for n in nums:
            if n in se:
                se.remove(n)
            else:
                se.add(n)
        return list(se)
