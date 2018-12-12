class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)<=10:
            return []
        seqcount={}
        for i in range(len(s)-9):
            if s[i:i+10] not in seqcount:
                seqcount[s[i:i+10]]=1
            else:
                seqcount[s[i:i+10]]+=1
        res=[]
        for seq in seqcount:
            if seqcount[seq]>1:
                res.append(seq)
        return res
