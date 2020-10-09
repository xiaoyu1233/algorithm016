class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []

        def backtrack(depth):
            if depth == len(nums):
                res.append(path[:])

            for i in range(len(nums)):
                if visited[i] == True:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == False:
                    continue
                visited[i] = True
                path.append(nums[i])
                backtrack(depth + 1)
                visited[i] = False
                path.pop()

        nums.sort()
        res = []
        path = []
        visited = [False for i in range(len(nums))]

        backtrack(0)
        return res
