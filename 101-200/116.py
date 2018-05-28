class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:return
        nodelist=[root]
        while len(nodelist)>0:
            nextlist=[]
            for i in range(len(nodelist)):
                if i<len(nodelist)-1:
                    nodelist[i].next=nodelist[i+1]
                if nodelist[i].left:
                    nextlist.append(nodelist[i].left)
                if nodelist[i].right:
                    nextlist.append(nodelist[i].right)
            nodelist=nextlist
