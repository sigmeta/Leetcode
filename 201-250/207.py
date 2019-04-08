class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        for p in prerequisites:
            graph[p[0]].append(p[1])
        cset=set()
        def dfs(cset,next_course):
            if not graph[next_course]:
                return True
            res=True
            for nc in graph[next_course]:
                if nc in cset:
                    return False
                if [next_course,nc] in prerequisites:
                    prerequisites.remove([next_course,nc])
                    graph[next_course].remove(nc)
                res=res and dfs(cset|{nc},nc)
            return res

        while prerequisites:
            if not dfs(cset|{prerequisites[0][0]},prerequisites[0][0]):
                return False
        return True
            
