import string
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        wordSet=set(wordList)
        def genNeighbor(w,wordSet):
            for i in range(len(w)):
                for l in string.ascii_lowercase:
                    nw=w[:i]+l+w[i+1:]
                    if nw in wordSet:
                        yield nw
        
        visited={beginWord}
        clist=[[] for i in range(len(wordList)+1)]
        clist[0]=[[beginWord]]
        for i in range(len(clist)-1):
            for j in range(len(clist[i])):
                for w in genNeighbor(clist[i][j][-1],wordSet):
                    if w==endWord:
                        return i+2
                    elif w in visited:
                        continue
                    else:
                        clist[i+1].append(clist[i][j]+[w])
                        visited.add(w)
        return 0
