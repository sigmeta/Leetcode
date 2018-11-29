class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1=[int(n) for n in version1.split('.')]
        v2=[int(n) for n in version2.split('.')]
        for i,j in zip(v1,v2):
            if i<j:
                return -1
            if i>j:
                return 1
        if len(v1)<len(v2) and sum(v2[len(v1):])>0:
            return -1
        elif len(v1)>len(v2) and sum(v1[len(v2):])>0:
            return 1
        else:
            return 0
