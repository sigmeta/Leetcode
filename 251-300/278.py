# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=0;r=n
        while l<r:
            m=(l+r)//2
            if not isBadVersion(m):
                if isBadVersion(m+1):
                    return m+1
                else:
                    l=m
            else:
                r=m
