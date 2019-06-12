class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s)<2:
            return s
        def isPalindrome(st):
            halflen=len(st)//2
            #print(st,st[:halflen],st[::-1][:halflen])
            return st[:halflen]==st[::-1][:halflen]
        clen=1
        for i in range(1,len(s)):
            if isPalindrome(s[:i+1]):
                clen=i+1
                #print(clen)
        return s[clen:][::-1]+s
