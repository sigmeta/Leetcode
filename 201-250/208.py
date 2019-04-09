class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree={}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t=self.tree
        for c in word:
            if c not in t:
                t[c]={}
            t=t[c]
        t['terminal']=None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        t=self.tree
        for c in word:
            if c not in t:
                return False
            t=t[c]
        if 'terminal' in t:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t=self.tree
        for c in prefix:
            if c not in t:
                return False
            t=t[c]
        return  True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
