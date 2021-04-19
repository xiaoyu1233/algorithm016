'''
Floyd法
求任意两点间的最短距离

核心思想：
逐渐添加中间点，查看是否存在最短路径，具体解释看博客园。
'''


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        graph = defaultdict(int)
        set1 = set()
        for i in range(len(equations)):
            a, b = equations[i]
            graph[(a, b)] = values[i]
            graph[(b, a)] = 1 / values[i]
            set1.add(a)
            set1.add(b)

        arr = list(set1)
        for k in arr:
            for i in arr:
                for j in arr:
                    if graph[(i, k)] and graph[(k, j)]:
                        graph[(i, j)] = graph[(i, k)] * graph[(k, j)]

        res = []
        for x, y in queries:
            if graph[(x, y)]:
                res.append(graph[(x, y)])
            else:
                res.append(-1)
        return res


'''
DFS
深度优先搜索
先建图，再搜索。
'''


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 构造图，equations的第一项除以第二项等于value里的对应值，第二项除以第一项等于其倒数
        '''
        graph = {}
        for (x, y), v in zip(equations, values):
            if x in graph:
                graph[x][y] = v
            else:
                graph[x] = {y: v}
            if y in graph:
                graph[y][x] = 1/v
            else:
                graph[y] = {x: 1/v}
        '''
        from collections import defaultdict
        graph = defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1 / val

        # dfs找寻从s到t的路径并返回结果叠乘后的边权重即结果
        def dfs(s, t) -> int:
            if s not in graph:
                return -1
            if t == s:
                return 1
            for node in graph[s].keys():
                if node == t:
                    return graph[s][node]
                elif node not in visited:
                    visited.add(node)  # 添加到已访问避免重复遍历
                    v = dfs(node, t)
                    if v != -1:
                        return graph[s][node] * v
            return -1

        # 逐个计算query的值
        res = []
        for qs, qt in queries:
            visited = set()
            res.append(dfs(qs, qt))
        return res

'''
BFS
广度优先搜索
'''
class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # construct directed graph
        graph = defaultdict(lambda: defaultdict(int))
        for (x, y), v in zip(equations, values):
            graph[x][y] = v
            graph[y][x] = 1/v


        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1
            if start==end:
                return 1
            queue = deque()
            queue.append((start, 1))
            visited.add(start)
            while queue:
                node, val = queue.popleft()
                if node==end:
                    return val
                for n in graph[node]:
                    if n in visited:
                        continue
                    visited.add(n)
                    queue.append((n, val*graph[node][n]))
            return -1

        res = []
        for start, end in queries:
            visited = set()
            query_res = bfs(start, end)
            res.append(query_res)
        return res


'''
并查集
'''
from collections import namedtuple, defaultdict

class Solution:
    def calcEquation(self, equations, values, queries) :
        class Item:
            def __init__(self, parent, value):
                self.parent = parent
                self.value = value

        father = defaultdict(Item)

        def find(x):
        #返回值为根节点
        #如果它是独立元素，根节点是自身，返回自己。不然，递归找到根节点，用路径压缩修改parent，并返回根节点。
            if x != father[x].parent:
                t = father[x].parent
                father[x].parent = find(t)
                father[x].value *= father[t].value  #1---3的权重就是（1--2的权重）*（2---3的权重）
                return father[x].parent
            return x

        def union(e1, e2, result):
            # 平行四边形法则边 (e1, e2), (e1, f1), (e2, f2) --> (f1, f2)
            #找到根节点判断是否相等
            f1 = find(e1)
            f2 = find(e2)
            #分别属于两个集合，需要合并：
            if f1 != f2:
                father[f1].parent = f2  #第一个根节点指向第二个根节点
                #更新权重，具体方法通过上面的例子可以算一下
                father[f1].value = father[e2].value * result / father[e1].value

        #用字典提高效率，判断是否见过
        number = defaultdict(int)

        #初始化：每个节点的父节点初始化为自身，不指向任何人，value为1
        for i,item in enumerate(equations) :
            s1, s2 = item[0], item[1]
            if s1 not in number:
                number[s1] =  1
                father[s1] = Item(parent=s1, value=1)
            if s2 not in number:
                number[s2] =  1
                father[s2] = Item(parent=s2, value=1)
            #根据两个节点的关系，合并两个节点。构建tree
            union(s1, s2, values[i])

        #开始计算：
        ans = []
        for s1, s2 in queries:
            #从来没见过，直接-1
            if s1 not in number or s2 not in number:
                ans.append(-1.0)
                continue
            #找到根节点，如果不想等，说明在不同集合tree中，没有任何关系，直接-1
            e1, e2 = s1, s2
            f1, f2 = find(e1), find(e2)
            if f1 != f2:
                ans.append(-1.0)
            else:
                #在同一个tree中
                v1 = father[e1].value
                v2 = father[e2].value
                #v1=e1/root   v2=e2/root  则e1/e2=v1/v2
                ans.append(v1 / v2)
        return ans

