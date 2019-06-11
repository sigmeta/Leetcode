from collections import OrderedDict, defaultdict
class Trie:
    def __init__(self):
        self.children=defaultdict(Trie)
        self.isEnd=False
    def addWord(self,word):
        if word=='':
            self.isEnd=True
            return
        self.children[word[0]].addWord(word[1:])

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root=Trie()
        self.res=set()
        self.R=len(board);self.C=len(board[0])
        for word in words:
            self.root.addWord(word)
        for i in range(self.R):
            for j in range(self.C):
                self.traverse(board,i,j,self.root,OrderedDict())
        return list(self.res)
    def traverse(self,board,i,j,node,visited):
        if node.isEnd:
            self.res.add(''.join(visited.values()))
        if i<0 or j<0 or i>=self.R or j>=self.C or board[i][j] not in node.children or (i,j) in visited:
            return
        visited[(i,j)]=board[i][j]
        self.traverse(board,i+1,j,node.children[board[i][j]],visited)
        self.traverse(board,i-1,j,node.children[board[i][j]],visited)
        self.traverse(board,i,j+1,node.children[board[i][j]],visited)
        self.traverse(board,i,j-1,node.children[board[i][j]],visited)
        del visited[(i,j)]
        
