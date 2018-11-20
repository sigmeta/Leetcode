# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        points=sorted(points,key=lambda k:k.x)
        lines={}
        for i in range(len(points)-1):
            same=[]
            
            for j in range(i+1,len(points)):
                if points[j].x == points[i].x and points[j].y == points[i].y:
                    same+=[points[i],points[j]]
                    a=None;b=points[i].x
                    continue
                elif points[j].y != points[i].y:
                    a = (points[j].x-points[i].x)/(points[j].y-points[i].y)
                    b = points[i].x-a*points[i].y
                else:
                    a = 'inf'
                    b = points[i].x
                if (a,b) not in lines:
                    lines[(a,b)]=set()
                lines[(a,b)].add(points[i])
                lines[(a,b)].add(points[j])
                for p in same:
                    lines[(a,b)].add(p)
            if not a:
                if (a,b) not in lines:
                    lines[(a,b)]=set()
                for p in same:
                    lines[(a,b)].add(p)
        if len(points)==0 or len(points)==1:
            return len(points)
        max=0
        for k in lines:
            if len(lines[k])>max:
                max=len(lines[k])
        return max
        
