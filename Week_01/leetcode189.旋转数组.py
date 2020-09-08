#暴力
#超时
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(k):
            temp = nums[-1]
            for i in range(len(nums)):
                nums[i],temp = temp,nums[i]
        return nums

#python技巧
#超22%
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(k):
            temp = nums.pop()
            nums.insert(0,temp)
        return nums

# python技巧
# 超85%
class Solution:
    def rotate(self,nums,k):
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]


#环状替换
#不会写

#反转数组
#超85%
class Solution:
    def reverse(self,nums,left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)





