#维护一个双端队列，建一个辅助栈，在队列上滑窗
#光头哥的解法太优美了
class Solution:
    def maxSlidingWindow(self, nums, k):
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += i,
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += nums[d[0]],
        return out


#动态规划

class Solution:
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        if n * k == 0: return []
        if k == 1: return nums
        left, right = [0] * n, [0] * n
        left[0] = nums[0]
        right[n - 1] = nums[n - 1]

        for i in range(1, n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])

            j = n - i - 1
            if (j + 1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])
        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))
        return output