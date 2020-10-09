#回溯法
#元素可以重复使用，所以向下回溯的时候inde不要直接后挪，要包含当前位
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates == []: return [[]]
        def backtrack(index):
            if sum(path) == target:
                res.append(path[:])
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                if sum(path) <= target:
                    backtrack(i)
                path.pop()
        path = []
        res = []
        backtrack(0)
        return res
