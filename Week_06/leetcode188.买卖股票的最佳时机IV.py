#https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/solution/gu-piao-jiao-yi-xi-lie-cong-tan-xin-dao-dong-tai-g/

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0

        if k >= n//2:   # 退化为不限制交易次数
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        else:           # 限制交易次数为k
            dp = [[[None, None] for _ in range(k+1)] for _ in range(n)]  # (n, k+1, 2)
            for i in range(n):
                dp[i][0][0] = 0
                dp[i][0][1] = -float('inf')
            for j in range(1, k+1):
                dp[0][j][0] = 0
                dp[0][j][1] = -prices[0]
            for i in range(1, n):
                for j in range(1, k+1):
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
            return dp[-1][-1][0]

