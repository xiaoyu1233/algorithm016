#方法一、双指针
#超过68%
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow,fast = 0,0
        for fast in range(len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]                
        return slow + 1
