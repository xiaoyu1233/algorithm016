#层序遍历。最适合的是使用队列结构进行广度优先搜索BFS，也可以进行深度优先搜索，记录好层数就行。
#BFS
#超84%
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        queue, res = [root, ], []
        while queue:
            temp = float("-inf")
            for _ in range(len(queue)):
                node = queue.pop(0)
                temp = max(temp, node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            res.append(temp)

        return res


#DFS
#超87%
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root, depth):
            if not root: return
            if len(res) == depth:
                res.append(float("-inf"))
            res[depth] = max(res[depth],root.val)
            if root.left is not None:
                dfs(root.left, depth + 1)
            if root.right is not None:
                dfs(root.right, depth + 1)
        dfs(root, 0)
        return res



