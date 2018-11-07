class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalindrome(s,l,r):
            while r>l:
                if s[l]!=s[r]:
                    return False
                l+=1;r-=1
            return True
        ans=[[] for i in range(len(s)+1)]
        ans[0].append([])
        for i in range(len(s)):
            for j in range(i+1):
                if isPalindrome(s,j,i):
                    for a in ans[j]:
                        ans[i+1].append(a+[s[j:i+1]])
        return ans[-1]
