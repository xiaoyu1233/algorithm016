#回溯法
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 0 or k == 0:
            return []

        def backtrace(index):
            if len(path) == k:
                res.append(path[:]) ##浅拷贝，这一步很重要

            for i in range(index,n):
                path.append(nums[i])
                backtrace(i + 1)
                path.pop()


        #先生成数
        nums = [i for i in range(1,n+1)]

        path = []
        res = []
        backtrace(0)
        return res

#python技巧
#Python itertools模块combinations(iterable, r)方法可以创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序。
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
         return list(itertools.combinations(range(1,n+1),k))
