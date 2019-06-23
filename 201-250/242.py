class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a1=[0]*26
        a2=[0]*26
        for c in s:
            a1[ord(c)-ord('a')]+=1
        for c in t:
            a2[ord(c)-ord('a')]+=1
        return a1==a2
