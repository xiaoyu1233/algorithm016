class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [0] * max((n + 1), 3)
        mod = 10 ** 9 + 7
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % mod

        result = 0
        for i in range(1, n // 2 + 1):
            result += (dp[i - 1] * dp[n - i]) % mod

        result *= 2
        if n % 2 == 1:
            result += dp[n // 2] * dp[n // 2]

        return (result + dp[n]) % mod
