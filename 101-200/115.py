class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        cnt = [1] + [0] * (len(t))
        for ch in s:
            for i in range(len(t)-1,-1,-1):
                if ch == t[i]:
                    cnt[i+1] += cnt[i]
        return cnt[-1]
        
