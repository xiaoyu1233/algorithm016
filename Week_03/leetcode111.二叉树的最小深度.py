#可以用递归和层序遍历做

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        min_depth = float('inf')
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)

        return min_depth + 1


#层序遍历

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        queue, res = [root,], 0
        if not root: return 0
        while queue:
            res += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                if not node: continue
                if not node.left and not node.right:
                    return res
                else:
                    queue.append(node.left)
                    queue.append(node.right)
        return res