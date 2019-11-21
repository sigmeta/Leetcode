class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        dct={}
        se=set()
        slist=str.split()
        if len(pattern)!=len(slist):
            return False
        for i,c in enumerate(pattern):
            if c in dct and dct[c]!=slist[i]:
                return False
            elif c not in dct and slist[i] in se:
                return False
            elif c not in dct:
                dct[c]=slist[i]
                se.add(slist[i])
        return True
