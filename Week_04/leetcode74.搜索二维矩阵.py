#二分法
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        # 二分查找
        left, right = 0, m * n - 1
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1
        return False

#右上角搜索法
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 从右上角开始寻找
        if not matrix:
            return False
        raws = len(matrix)
        cols = len(matrix[0])
        raw = 0
        col = cols - 1

        while 0 <= raw < raws and 0 <= col < cols:
            if matrix[raw][col] < target:
                raw += 1
            elif matrix[raw][col] > target:
                col -= 1
            else:
                return True
        return False


