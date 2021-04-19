#动态规划
class Solution:
    def longestCommonSubsequence(self, text1, text2) -> int:
        m, n = len(text1), len(text2)
        # 构建 DP table 和 base case
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 进行状态转移
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # 找到一个 lcs 中的字符
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
        return dp[-1][-1]


#空间优化
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        pre = [0] * (n + 1)
        cur = [0] * (n + 1)
        for i in range(1, m + 1):
            cur[0] = 0
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    cur[j] = pre[j - 1] + 1
                else:
                    cur[j] = max(pre[j], cur[j - 1])
            pre = cur[:]
        return cur[-1]

