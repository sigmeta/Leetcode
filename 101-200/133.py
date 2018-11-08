# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        node_dict={}
        def bfs(n):
            if n.label not in node_dict:
                rn=UndirectedGraphNode(n.label)
                node_dict[n.label]=rn
                for nei in n.neighbors:
                    rn.neighbors.append(bfs(nei))
                return rn
            else:
                return node_dict[n.label]
        return bfs(node)
