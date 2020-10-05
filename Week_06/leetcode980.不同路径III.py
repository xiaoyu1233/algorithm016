#回溯法
#写得漂亮。题目要求每条路径要遍历所有空格，那么就将最后可以遍历所有空格作为回溯结束的条件。同一条路径不允许有回头路，
#那么就将走过的路径标记为障碍，回退的时候再恢复。
#妙啊
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        steps,m,n = 1,0,0
        count = 0
        for r,row in enumerate(grid):
            for c,val in enumerate(row):
                if val == 1:
                    m,n = r,c
                if val == 0:
                    steps += 1

        def traceback(r,c,step):
            nonlocal count
            if  grid[r][c] == 2:
                if step == 0:
                    count += 1
                return
            grid[r][c] = -1
            for i,j in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0<=i<rows and 0<=j<cols and grid[i][j] != -1:
                    temp = grid[i][j]
                    traceback(i, j, step-1)
                    grid[i][j] = temp
        traceback(m, n, steps)
        return count
