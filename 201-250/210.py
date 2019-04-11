class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        src=[set() for _ in range(numCourses)]
        dst=[set() for _ in range(numCourses)]
        for d,s in prerequisites:
            src[d].add(s)
            dst[s].add(d)
        ans=[a for a in range(numCourses) if not src[a]]
        for s in ans:
            for d in dst[s]:
                src[d].remove(s)
                if not src[d]:
                    ans.append(d)
        return ans if len(ans)==numCourses else []
