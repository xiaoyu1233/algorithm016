#方法一、排序+双指针
#超过96%
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sort_num = nums.copy()
        sort_num.sort()
        left, right = 0, len(nums)-1
        while left < right:
            if sort_num[left] + sort_num[right] == target:
                break
            elif sort_num[left] + sort_num[right] > target:
                right -= 1
            else:
                left += 1
        a = nums.index(sort_num[left])
        nums.pop(a)
        b = nums.index(sort_num[right])
        if b >= a:
            b += 1
        return [a,b]

#方法二、哈希
#超过97%
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #sort+双指针
        #哈希
        hashMap = {}
        for i in range(len(nums)):
            if hashMap.get(target-nums[i]) is not None:
                return [hashMap.get(target-nums[i]),i]
            hashMap[nums[i]] = i

