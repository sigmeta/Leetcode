class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return False
        wordDict=set(wordDict)
        r=[set([]) for _ in range(len(s)+1)]
        r[0].add(-1)
        for i in range(len(s)):
            for n in r[i]:
                r[i+1].add(n)
                if s[n+1:i+1] in wordDict:
                    r[i+1].add(i)
        if max(r[-1])!=len(s)-1:
            return False
        else:
            return True
