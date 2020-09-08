#暴力
#超时
class Solution:
    def trap(self, height: List[int]) -> int:
        #边界条件
        n = len(height)
        for i in range(n):
            max_left, max_right = 0, 0
            for j in range(0,i):
                max_left = max(max_left,height[j])
            for j in range(i,range(height)):
                max_right = max(max_right,height[j])
            if min(max_left,max_right) > height[i]
                water += min(max_left,max_right)
        return water

#加memo
#超75%
class Solution():
    def trap(self, height):
        #边界条件，一定要判断，否则后面按照数组长度生成新数组的时候，如果为空，会产生溢出
        if not height: return 0
        n = len(height)#数组长
        water = 0#储水量
        max_left = [0] * n #每个位置处，从左向右的最大值
        max_right = [0] * n #每个位置处，从右向左的最大值
        max_left[0] = height[0] #设置初始值
        max_right[n - 1] = height[n - 1] #设置初始值
        for i in range(1, n): #求从左向右的最大值
            max_left[i] = max(max_left[i - 1], height[i])
        for j in range(n - 2, -1, -1): #求从右向左的最大值
            max_right[j] = max(max_right[j + 1], height[j])
        for i in range(n): #每个位置处，都可以表中拿到左边最大值和右边最大值
            if min(max_left[i], max_right[i]) > height[i]:
                water += min(max_left[i], max_right[i]) - height[i]
        return water

#双指针
#75%
class Solution:
    def trap(self, height: List[int]) -> int:
        #边界条件
        if not height:  return 0
        n = len(height)
        max_left = height[0] #左边的最大值，实时更新
        max_right = height[n-1] #右边的最大值，实时更新
        left,right = 0,n-1 #左右双指针
        water = 0 #储水量
        while left < right:
            max_left = max(max_left,height[left]) #每个点都更新，保证是最大值
            max_right = max(max_right,height[right]) #从外向内更新
            if max_left < max_right: #小的一边决定储水量的多少，左边较低，说明
                                     #左边能储存的水最多就这些了，更新左边值，移动指针
                water += max_left - height[left]
                left += 1
            else:
                water += max_right -height[right] #右边较低，说明右边存储的水最多就这些
                right -= 1
        return water


