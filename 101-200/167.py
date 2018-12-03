class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm={}
        for i,n in enumerate(numbers):
            if target-n in hm:
                return [hm[target-n],i+1]
            else:
                hm[n]=i+1
