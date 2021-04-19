#贪心
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

#谷底买入，峰顶卖出
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        flag=False##是否持有股票
        profit=0
        buy_point=0
        for i in range(len(prices)-1):
            if prices[i] > prices[i+1] and flag == False:##处于下降数列中，不买入
                continue
            elif prices[i] < prices[i+1] and flag == False:##记录谷底，买入
                buy_point = i
                flag = True
                。
            if prices[i] < prices[i+1] and flag == True:##处于上升数列中，不卖出
                continue
            elif prices[i] > prices[i+1] and flag == True:##峰顶，卖出
                profit += prices[i] - prices[buy_point]
                flag = False
        if  flag == True:##如果在结束仍然持有股票，则在最后一天卖出（由于在下降数列中不会买入，此时必然是高于买入价的）
            profit += prices[-1] - prices[buy_point]
        return profit

