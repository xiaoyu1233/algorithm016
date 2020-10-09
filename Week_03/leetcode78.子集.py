#leetcode题解里有篇总结特别好
#https://leetcode-cn.com/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/

#python技巧
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)+1):
            for tmp in itertools.combinations(nums, i):
                res.append(tmp)
        return res

#迭代
#这个写法太python了，优美！
#新元素增加的新的组合，就是前面元素所有的组合再加上这个元素，再将新元素增加的组合融合进组合总体中，进入下一轮循环。
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res

#回溯
#套模板
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []: return [[]]

        def backtrack(idx):
            # 不需要等一条路径回溯结束再保存值，每一步都要保存值。
            ans.append(path[:])
            for i in range(idx, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        path = []
        res = []
        backtrack(0)
        return res

#回溯的另一种写法，因为再回溯的时候将每一层的结果都传递下去了，相当于每一层重写赋值path，
#因此不向回撤也可以，相当于自动回撤，这对于空间的占用较高。
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp) #把上层结果添加到res里
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])  #向下递归，并把本层结果传递到下一层

        helper(0, [])
        return res



