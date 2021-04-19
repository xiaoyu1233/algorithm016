#DFS
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(cur,n,res): # cur为根结点
            if cur > n:
                return
            else:
                res.append(cur)
                for i in range(10):
                    if 10 * cur + i > n: # 比如叶子结点为14，而n是13，dfs就结束了
                        return
                    dfs(10 * cur + i, n, res)
        res = []
        # 对每棵树进行dfs
        for i in range(1,10):
            dfs(i, n, res)
        return res

