#贪心

#从当前点进行一次跳跃，然后将end的边界拉到本次跳跃最远的边界，遍历这个区间内第二次跳跃能到达的最远点，
#当这个区间遍历结束后，更新最远点，将end拉到这个最远点。跳跃次数+1。
#最后一个点不用跳，直接到达就行
#所以遍历到n - 1就行

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False

#