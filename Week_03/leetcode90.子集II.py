#回溯法
#套模板，在子集I上加一个去重条件即可，去重记得先排序数组
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if nums == []: return [[]]

        def backtrack(idx):
            # 不需要等一条路径回溯结束再保存值，每一步都要保存值。
            res.append(path[:])
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        nums.sort()
        path = []
        res = []
        backtrack(0)
        return res