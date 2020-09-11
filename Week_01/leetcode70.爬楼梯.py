#纯递归
#超时，到38就递归不下去了
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)


#加memo的递归
#超过99%
class Solution:
    memo = {}#搞个字典，后面用的时候记得加self啊，类成员变量。
    def climbStairs(self, n: int) -> int:
        if n ==1: return 1
        if n ==2: return 2
        if self.memo.get(n) is not None:
            return self.memo[n]#有了就别再递归算了，直接从字典拿数多香
        self.memo[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        #新数咱得存一下
        return self.memo[n]

#数组+通项式
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):#循环从2往后写啊，之前的不能计算，要不然会被全部覆盖为0的。
            dp[i] = dp[i-1]+dp[i-2]
            #print(i,dp[i])
        return dp[n]

#简化空间
class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        for _ in range(n):
            a,b = b, a+b
        return a

while True:
    print('祝老师节日快乐！')
