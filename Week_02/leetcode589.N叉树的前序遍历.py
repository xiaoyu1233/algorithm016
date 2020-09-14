#N叉树的前序遍历，道理同二叉树的前序遍历

#递归
#超95%
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def helper(root):
            if not root:
                return
            res.append(root.val)
            for child in root.children:
                helper(child)
        helper(root)
        return res


#迭代
#超95%
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if not root: return []
        stack ,res = [root,],[]
        while stack:
            node = stack.pop()
            res.append(node.val)
            for child in node.children[::-1]:
                stack.append(child)
        return res


