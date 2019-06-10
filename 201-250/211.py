class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s={}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        s=self.s
        for i in range(len(word)):
            if i<len(word)-1:
                if word[i] not in s:
                    s[word[i]]={word[i+1]:{}}
                elif word[i+1] not in s[word[i]]:
                    s[word[i]][word[i+1]]={}
            else:
                if word[i] not in s:
                    s[word[i]]={'END':{}}
                else:
                    s[word[i]]['END']={}
            s=s[word[i]]

    def search(self, word: str, s=None) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if s==None:
            s=self.s
        if word=='':
            return 'END' in s
        if word[0]!='.' and word[0] not in s:
            return False
        elif word[0] !='.':
            return self.search(word[1:],s[word[0]])
        else:
            res=False
            for k in s:
                res=res or self.search(word[1:],s[k])
            return res
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
