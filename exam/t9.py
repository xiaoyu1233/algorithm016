#1,2,2,4,4,5,5,5,10,12
left,right = 0, 0
class Solution:
    def findLowerUpper(self, nums, target) :
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                break
        target_inex = mid
        for i in range(target_inex, -1, -1):
            if nums[target_inex] == target:
                target_inex -= 1
            else:
                break
            lower = i
        for j in range(target_inex + 1):
            if nums[target_inex] == target:
                target_inex += 1
            else:
                break
            upper = j
        return [lower, upper]
