class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict={}
        for n in nums:
            if n in num_dict:
                continue
            if n+1 in num_dict and n-1 in num_dict:
                new_len=num_dict[n-1]+num_dict[n+1]+1
                num_dict[n]=new_len
                num_dict[n-num_dict[n-1]]=new_len
                num_dict[n+num_dict[n+1]]=new_len
            elif n-1 in num_dict:
                new_len=num_dict[n-1]+1
                num_dict[n]=new_len
                num_dict[n-num_dict[n-1]]=new_len
            elif n+1 in num_dict:
                new_len=num_dict[n+1]+1
                num_dict[n]=new_len
                num_dict[n+num_dict[n+1]]=new_len
            else:
                num_dict[n]=1
        m=0
        for n in num_dict:
            if num_dict[n]>m:
                m=num_dict[n]
        return m
