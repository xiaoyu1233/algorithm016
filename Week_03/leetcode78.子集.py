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
lass Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res

#回溯
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



