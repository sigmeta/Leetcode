class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        l,r=0,len(s)-1
        while l<r:
            if not ('a'<=s[l]<='z' or '0'<=s[l]<='9'):
                l+=1
                continue
            if not ('a'<=s[r]<='z' or '0'<=s[r]<='9'):
                r-=1
                continue
            if s[l]==s[r]:
                l+=1;r-=1
            else:
                return False
        return True
