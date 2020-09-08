#双指针
#超过85%
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0, len(height)-1
        res = 0
        while left < right:
            if height[left] < height[right]:
                res = max(res,height[left]*(right-left))
                left += 1
            else:
                res = max(res,height[right]*(right-left))
                right -= 1
        return res