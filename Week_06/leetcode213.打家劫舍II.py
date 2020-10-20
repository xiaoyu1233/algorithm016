#DP
class Solution:
    def rob(self, nums: List[int]) -> int:
        def myrob(nums: List[int]) -> int:
            if not nums:
                return 0

            size = len(nums)
            if size == 1:
                return nums[0]

            dp = [0] * size
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, size):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

            return dp[-1]
        return max(myrob(nums[1:]), myrob(nums[:-1])) if len(nums) > 1 else nums[0]	

#和打家劫舍I是同一思路，分为第一个房子不偷和最后一个房子不偷的情况
class Solution:
    def rob(self, nums: [int]) -> int:
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur
        return max(my_rob(nums[:-1]),my_rob(nums[1:])) if len(nums) > 1 else nums[0]

