from collections import deque
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited={0}
        queue=deque([(0,0)])
        while queue:
            cut,idx=queue.popleft()
            if s[idx:]==s[idx:][::-1]:
                return cut
            for i in range(idx+1,len(s)+1):
                if i not in visited and s[idx:i]==s[idx:i][::-1]:
                    visited.add(i)
                    queue.append((cut+1,i))
