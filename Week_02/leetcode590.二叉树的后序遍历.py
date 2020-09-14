#二叉树的后序遍历，用递归和迭代两种方法做
#后续遍历的迭代方法是先保存根-右-左的值，然后倒序输出，就是左-右-根的顺序了。
#压栈的时候是存根，压左-右，出栈顺序就变成了右-左，所以，保存的顺序是根-右-左。
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
    def postorder(self, root):
        res = []
        def helper(root):
            if not root:
                return
            for child in root.children:
                helper(child)
            res.append(root.val)
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

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            for c in root.children:
                stack.append(c)
        return output[::-1]


