#暴力
class Solution():
    def longestPalindrome(self,s):
        #边界条件，主要是要判断字符串不能为空，否则下标会溢出
        if s == s[::-1]: return s #
        max_length = 1 #初始化，要更新的字串长度
        res = s[0] #初始字串
        for i in range(0,len(s)-1):#遍历数组，注意下标
            for j in range(i+1,len(s)): #遍历，注意下标
                #判断是否存在新子串更长，如果存在，则更新最长字串长和最长字串
                #使用了python的切片方式来判断字串是否相同，导致时间复杂度O(n^2)
                #如果不用切片，则是否为回文仍需要一次遍历来判断，复杂度为O(n^3)
                if j-i+1 > max_length and s[i:j+1]==s[i:j+1][::-1]:
                    max_length = j-i+1 #更新最长字串长
                    res = s[i:j+1] #更新最长字串
        return res
    
#DP
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)#字符串的长
        dp = [[False] * n for _ in range(n)]#构建一个矩阵，初始值全部为False
        #纵向是i坐标，横向是j坐标，因为j始终大于i所以这个矩阵只用填右上角
        ans = ""#记录最长回文字串
        #先升序填列，再升序填行
        for j in range(0,n):
            #升序降序填列都行，因为是前一列填好才对后一列进行求解
            for i in range(j,-1,-1): #for i in range(0,j+1):
                #先进行了两个判断，可以排除下标溢出
                #本质原因，动态规划需要初始条件，有内部是否为回文来决定外部是否是回文
                #初始条件1，最初始的字符是单字符，则一定构成字符串
                if j == i :dp[i][j]=True
                #初始条件2，最初始的字符是双字符，则是否为回文由这两个字符是否相等决定
                elif j - i == 1:
                    dp[i][j] = (s[i] == s[j])
                #d[i][j]代表的是有i到j的字符串是否为回文的状态
                #i到j是否为回文由i+1到j-1和新增的两个值决定
                #dp[i][j]的状态由dp[i + 1][j - 1]和s[i] == s[j]决定
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and j-i+1>len(ans):
                    ans = s[i:j+1]
        return ans
    
#DP空间优化

class Solution():
    def longestPalindrome(self,s):
        n = len(s)
        line = [False]*n #维护一列数组，不断更新，道理相同。
        ans=""
        for j in range(0,n):
            for i in range(0,j+1):
                if j == i: line[i] = True
                elif j - i == 1:
                    line[i] = s[i]==s[j]
                else:
                    line[i] = line[i+1] and s[i]==s[j]
                if line[i] and j-i+1>len(ans):
                    ans = s[i:j+1]
        return ans
    
#中心扩散法
class Solution():
    def expandAroundCenter(self,s, left, right):
        #从中心开始向两边依次检测是否相等
        while left >= 0 and right < len(s) and s[left]==s[right]:
            left -= 1
            right += 1
        return left+1, right-1
    def longestPalindrome(self,s):
        start, end =0, 0
        for i in range(len(s)):
            #中心扩散分为奇数中心和偶数中心，如"bab","baab"
            left1, right1 = self.expandAroundCenter(s,i ,i)
            left2, right2 = self.expandAroundCenter(s, i, i+1)
            #更新最长回文串首尾
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 -left2 > end - start:
                start, end = left2, right2
        return s[start:end+1]
    
    