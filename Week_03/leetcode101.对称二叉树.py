#递归
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        def helper(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return helper(left.left, right.right) and helper(left.right, right.left)
        return helper(root.left, root.right)




#迭代
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        queue = collections.deque()
        queue.append((root.left,root.right))
        while queue:
            left,right = queue.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            queue.append((left.left,right.right))
            queue.append((left.right,right.left))
        return True