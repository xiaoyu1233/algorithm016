# import copy
# rows, cols = map(int, input().split())
# # print(rows, cols,type(rows))
# matrix = []
# for i in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)


nums = int(input())
res = []
for i in range(nums):
    row = list(map(int, input().split()))
    n, k = row[0], row[1]
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):  # 循环从2往后写啊，之前的不能计算，要不然会被全部覆盖为0的。
         dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
         for j in range(1, k):
             if i - 3 * k == 0:
                 dp[i] = dp[i] - dp[(i - 3) * j - 3 * j]
             if i - 3 * k > 0:

                 dp[i] = dp[i] - dp[(i - 1) * j - 3 * j] - dp[(i - 2) * j - 3 * j] - dp[(i - 3) * j - 3 * j]

             print(i,dp[i])
    ans = dp[-1] % 100007
    res.append(ans)
for num in res:
    print(num)
