#DP，常规思路
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_temp = nums[0]
        sum_max = sum_temp

        for i in range(1, len(nums)):
            if sum_temp > 0:
                sum_max = max(sum_max, sum_temp + nums[i])
                sum_temp = sum_temp + nums[i]

            else:
                sum_max = max(sum_max, nums[i])
                sum_temp = nums[i]
        return sum_max


#DP+技巧
#数组中每个位置存的是以当前值为结尾的最大子序列和，因此最后求max就得到整个数组中的最大子序列和。
#写法1
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1] + nums[i], nums[i])
        return max(nums)

#写法2
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[0]*(len(nums))
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            if dp[i-1]<=0:
                dp[i]=nums[i]
            else:
                dp[i]=dp[i-1]+nums[i]
        return max(dp)


#分治
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # 递归终止条件
        if n == 1:
            return nums[0]
        else:
            # 递归计算左半边最大子序和
            max_left = self.maxSubArray(nums[0:len(nums) // 2])
            # 递归计算右半边最大子序和
            max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])

        # 计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        # 返回三个中的最大值
        return max(max_right, max_left, max_l + max_r)


