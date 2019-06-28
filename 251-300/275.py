class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h=0
        for i,n in enumerate(citations[::-1]):
            if i+1<=n:
                h=i+1
        return h
