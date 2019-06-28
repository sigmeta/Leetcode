class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cit=sorted(citations,reverse=True)
        h=0
        for i,n in enumerate(cit):
            if i+1<=n:
                h=i+1
        return h
