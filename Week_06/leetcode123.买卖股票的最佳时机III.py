#用第一次的钱抵消一部分第二次买的钱
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = float('inf')  # 第一二次买之前的最低价
        pro1 = pro2 = 0

        for price in prices:
            buy1 = min(buy1, price)
            pro1 = max(pro1, price - buy1)
            buy2 = min(buy2, price - pro1)  # 第一次赚的钱用来补贴第二次
            pro2 = max(pro2, price - buy2)
        return pro2

#顺逆两次遍历
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        minPri, maxPro1 = prices[0], 0      # 顺序遍历的最小pirce和最大利润
        maxPri, maxPro2 = prices[-1],0      # 逆序遍历的最大price和最大利润
        profit1, profit2 = [0] * n, [0] * n # 顺序和逆序的利润分布
        for i in range(n):
            if prices[i] <= minPri: minPri = prices[i]
            else: maxPro1 = max(maxPro1, prices[i]-minPri)
            profit1[i] = maxPro1
            if prices[n-i-1] >= maxPri: maxPri = prices[n-i-1]
            else: maxPro2 = max(maxPro2, maxPri-prices[n-i-1])
            profit2[n-i-1] = maxPro2
        maxPro = profit1[-1]
        for i in range(n-1):
            maxPro = max(maxPro, profit1[i]+profit2[i+1])
        return maxPro


#链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/shun-ni-liang-ci-bian-li-qiu-jie-by-fxyz-0/

