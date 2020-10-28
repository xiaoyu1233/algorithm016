#插入值
#打印，中序遍历
#递归

#树节点定义
class TreeNode():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    #插入
    def insertNum(self,root,val):
        if root == None:
            root = TreeNode(val)

        elif val < root.val:
            root.left = self.insertNum(root.left, val)
        elif val > root.val:
            root.right = self.insertNum(root.right, val)
        return root
    #打印
    def printTree(self,root):
        if root == None:
            return
        self.printTree(root.left)
        print(root.val,', ', end = '')
        self.printTree(root.right)

#要插入的数组
nums = [1,80,6,7,3,2]

tree1 = Solution()
#插入
for i in range(len(nums)):
    if i == 0:
        tree1_root = tree1.insertNum(None,nums[i])
    else:
        tree1.insertNum(tree1_root,nums[i])
#打印
tree1.printTree(tree1_root)

