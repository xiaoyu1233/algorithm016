#二维DP
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not 
        r, c = len(grid), len(grid[0])
        dp = [[0] * c for _ in range(r)]
        dp[0][0] = grid[0][0]

        for i in range(1, r):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, c):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, r):
            for j in range(1, c):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        #print(dp)
        return dp[-1][-1]

#空间优化
O(n)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        r, c = len(grid), len(grid[0])
        dp = [0] * c 
        dp[0] = grid[0][0]

        for j in range(1, c):
            dp[j] = dp[j - 1] + grid[0][j]

        for i in range(1, r):
            dp[0] += grid[i][0] 
            for j in range(1, c):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        #print(dp)
        return dp[-1]