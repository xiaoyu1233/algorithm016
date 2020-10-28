class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if not A: return 0

        length = len(A)

        left, right = [0] * length, [0] * length

        for i in range(1, length):
            left[i] = left[i - 1] + 1 if A[i] > A[i - 1] else 0
        for i in range(length - 2, -1, -1):
            right[i] = right[i + 1] + 1 if A[i] > A[i + 1] else 0

        res = 0
        for i in range(1, length - 1):
            if left[i] > 0 and right[i] > 0:
                res = max(res, left[i] + right[i] + 1)
        return res


