class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist=s.split()
        slist.reverse()
        return ' '.join(slist)
