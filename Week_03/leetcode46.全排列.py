class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []
        def backtrack(depth):
            if depth == len(nums):
                res.append(path[:]) #记得加冒号，否则是添加的引用，无法真正将值存下来。
            for i in range(len(nums)):
                if not visited[i]: #遍历备选值，如果值用过了，那么这个值不选。
                    visited[i] = True
                    path.append(nums[i])
                    backtrack(depth + 1)
                    visited[i] = False
                    path.pop()

        visited = [False for i in range(len(nums))]
        res = []
        path = []
        backtrack(0)
        return res