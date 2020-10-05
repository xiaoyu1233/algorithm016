#动态规划
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [[0] * n for _ in range(n)]
        f[0][0] = triangle[0][0]

        for i in range(1, n):
            f[i][0] = f[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
            f[i][i] = f[i - 1][i - 1] + triangle[i][i]

        return min(f[n - 1])

#动态规划+空间优化
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [0] * n
        f[0] = triangle[0][0]

        for i in range(1, n):
            f[i] = f[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                f[j] = min(f[j - 1], f[j]) + triangle[i][j]
            f[0] += triangle[i][0]

        return min(f)


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