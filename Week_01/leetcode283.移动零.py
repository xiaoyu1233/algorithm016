#双指针
#超过85%
class Solution():
    def moveZeroes(self, nums: List[int]) -> None:
	    slow,fast = 0,0
	    for fast in range(len(nums)):
	    	if nums[fast] != 0:
	    		nums[slow],nums[fast] = nums[fast],nums[slow]
	    		slow += 1

#python技巧
#超过10%
class Solution():
    def moveZeroes(self, nums: List[int]) -> None:
	    for num in nums:
	    	if num == 0:
	    		nums.remove(0)
	    		nums.append(0)
	    return nums
