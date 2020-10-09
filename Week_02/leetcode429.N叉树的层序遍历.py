#层序遍历。最适合的是使用队列结构进行广度优先搜索BFS，也可以进行深度优先搜索，记录好层数就行。
#BFS
#超74%
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None: return []
        queue, res = [root,], []
        while queue:
            sub_res = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                sub_res.append(node.val)
                for child in node.children:
                    queue.append(child)
            res.append(sub_res)
        return res


#DFS
#超74%
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        def dfs(root, depth):
            if not root: return
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            for ch in root.children:
                dfs(ch, depth + 1)
        dfs(root, 0)
        return res



