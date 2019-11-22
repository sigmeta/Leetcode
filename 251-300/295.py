import bisect
class MedianFinder:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.li=[]

    def addNum(self, num: int) -> None:
        bisect.insort(self.li,num)

    def findMedian(self) -> float:
        if not self.li:
            return 0
        if len(self.li)%2==0:
            return (self.li[len(self.li)//2]+self.li[len(self.li)//2-1])/2
        else:
            return self.li[len(self.li)//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()