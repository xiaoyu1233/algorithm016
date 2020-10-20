#动态规划
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int: 
        r = len(triangle)
        dp = [[0] * r for _ in range(r)]
        dp[0][0] = triangle[0][0]
        for i in range(1, r):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
        return min(dp[-1])


#动态规划+空间优化
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int: 
        r = len(triangle)
        dp = [0] * r
        dp[0] = triangle[0][0]
        for i in range(1, r):
            dp[i] = dp[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                dp[j] = min(dp[j], dp[j -1]) + triangle[i][j]
            dp[0] += triangle[i][0]
        return min(dp)



#高赞回答
# O(n*n/2) space, top-down
def minimumTotal1(self, triangle):
    if not triangle:
        return
    res = [[0 for i in xrange(len(row))] for row in triangle]
    res[0][0] = triangle[0][0]
    for i in xrange(1, len(triangle)):
        for j in xrange(len(triangle[i])):
            if j == 0:
                res[i][j] = res[i - 1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                res[i][j] = res[i - 1][j - 1] + triangle[i][j]
            else:
                res[i][j] = min(res[i - 1][j - 1], res[i - 1][j]) + triangle[i][j]
    return min(res[-1])


# Modify the original triangle, top-down
def minimumTotal2(self, triangle):
    if not triangle:
        return
    for i in xrange(1, len(triangle)):
        for j in xrange(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
    return min(triangle[-1])


# Modify the original triangle, bottom-up
def minimumTotal3(self, triangle):
    if not triangle:
        return
    for i in xrange(len(triangle) - 2, -1, -1):
        for j in xrange(len(triangle[i])):
            triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]


# bottom-up, O(n) space
def minimumTotal(self, triangle):
    if not triangle:
        return
    res = triangle[-1]
    for i in xrange(len(triangle) - 2, -1, -1):
        for j in xrange(len(triangle[i])):
            res[j] = min(res[j], res[j + 1]) + triangle[i][j]
    return res[0]