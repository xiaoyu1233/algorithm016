#回溯法
#元素有重复需要去重，每次遇到重复的值即跳过，并且保证备选数组的第一个值永远是可选的。
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates == []: return [[]]
        def backtrack(index):
            if sum(path) == target:
                res.append(path[:])
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                if sum(path) <= target:
                    backtrack(i + 1)
                path.pop()
        path = []
        res = []
        candidates.sort()
        backtrack(0)
        return res
