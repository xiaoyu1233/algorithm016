class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n + 1) #dp[i]表示s从下标长度为i的字符串的方法总数
        dp[0] = 1
        dp[1] = 1 if s[0]!="0" else 0

        for i in range(2, n + 1):
            if s[i - 1] == '0':
                if 0 < int(s[i - 2]) <= 2:
                    dp[i] = dp[i - 2]
                else:
                    dp[i] = 0
            else:
                if 10 < int(s[i - 2] + s[i - 1]) <= 26:
                    dp[i] = dp[i - 2] + dp[i - 1]
                else:
                    dp[i] = dp[i - 1]
        return dp[-1]
