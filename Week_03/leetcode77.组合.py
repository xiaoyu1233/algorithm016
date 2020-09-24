
#回溯法
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ##先生成数
        nums = [i for i in range(1,n+1)]
        # print(nums)

        ##明显用回溯法:
        res = []

        def backtrace(nums_b,curr_res,index):
            # print("curr_res:",curr_res)
            if len(curr_res)==k:
                res.append(curr_res[:]) ##浅拷贝，这一步很重要
                return

            for i in range(index,n):
                # print(i,nums_b)
                curr_res.append(nums[i])
                backtrace(nums_b[index:],curr_res,i+1)
                curr_res.pop()

        ##特殊情况处理
        if n==0 or k==0:
            return res

        backtrace(nums,[],0)
        return res

#python技巧
#Python itertools模块combinations(iterable, r)方法可以创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序。
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
         return list(itertools.combinations(range(1,n+1),k))
