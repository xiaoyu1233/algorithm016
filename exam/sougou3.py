# class Solution:
#     def calcProb(self , n ):
#         # write code here
#         if n < 4: return 1
#         else: return 0.5
class Solution:
    def calcProb(self, n):
        # write code here
        dp = [0] * (n + 1)
        if n < 4:  return 1
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        dp[3] = 1

        for i in range(4, n + 1):
            dp[i] = max((1 - (dp[i - 1] * 0.5 + dp[i- 2] * 0.5)),
                        (1 - (dp[i - 2] * 0.5 + dp[i - 3] * 0.5)),
                        (1 - (dp[i - 3] * 0.5 + dp[i - 4] * 0.5)))
            # print( "a", (1 - (dp[i - 1] * 0.5 + dp[i - 2] * 0.5)),
            #             (1 - (dp[i - 2] * 0.5 + dp[i - 3] * 0.5)),
            #             (1 - (dp[i - 3] * 0.5 + dp[i - 4] * 0.5)))
            print('第',i,dp[i])
        return dp[n]

a = Solution()
#a.calcProb(4)
c= a.calcProb(20)
print(c)
