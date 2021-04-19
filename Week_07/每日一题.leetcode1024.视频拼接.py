
#DP
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        dp = [float('inf')] * (T + 1)
        dp[0] = 0

        for i in range(1, T + 1):
            for start, end in clips:
                if start < i <= end:
                    dp[i] = min(dp[i], dp[start] + 1)
        return -1 if dp[T] == float('inf') else dp[i]

#贪心
#跳跃游戏
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        step = [0] * T
        start = rightmost = 0
        res = 0

        # 记录从每一步起点开始能跳跃到的最远位置
        for begin, end in clips:
            if begin < T:
                step[begin] = max(step[begin], end)

        for i in range(T):
            rightmost = max(rightmost, step[i])

            if i == rightmost:
                return -1
            if i == start:
                res += 1
                start = rightmost
        return res

