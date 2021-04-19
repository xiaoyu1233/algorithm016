#暴力
#双指针
def findindex(nums):
    if nums == []: return -1
    left, right = 0, len(nums) - 1
    left_sum, right_sum = 0, 0
    while left < right:
        # left_sum += nums[left]
        # right_sum += nums[right]
        if left_sum == right_sum:
            if left + 1 == right - 1:
                return left + 1
            else:
                right -= 1
                right_sum += nums[right]
        elif left_sum > right_sum:
            right -= 1
            right_sum += nums[right]
        else:
            left += 1
            left_sum += nums[left]
    return -1


nums1 = [1,2,3,2,1]
nums2 = [0, 0, 0, 0]
nums3 = [-10000,10000,1,10000,-10000]
nums4 = []
res1 = findindex(nums1)
res2 = findindex(nums2)
res3 = findindex(nums3)
res4 = findindex(nums4)
print(res1, res2, res3, res4)