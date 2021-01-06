#自己写的
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        l = len(A)
        i = 1
        while i < len(A):
            if A[i] > A[i - 1]:
                i += 1
            else:
                break
        if i == len(A) or i == 1: return False
        while i < len(A):
            if A[i] < A[i - 1]:
                i += 1
            else:
                return False
        return True

#官方题解
class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # 递增扫描
        while i + 1 < N and A[i] < A[i + 1]:
            i += 1

        # 最高点不能是数组的第一个位置或最后一个位置
        if i == 0 or i == N - 1:
            return False

        # 递减扫描
        while i + 1 < N and A[i] > A[i + 1]:
            i += 1

        return i == N - 1

