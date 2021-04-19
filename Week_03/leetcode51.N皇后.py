#N皇后

#回溯法，套模板
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0: return []
        def backtrack(depth):
            if depth == n:
                res.append(path[:])
            for i in range(n):
                if cols[i] == False and hill_diagonals[depth + i] == False and dale_diagonals[depth - i] == False:
                    cols[i] = True
                    hill_diagonals[depth + i] = True
                    dale_diagonals[depth - i] = True
                    path.append(i)
                    backtrack(depth + 1)

                    cols[i] = False
                    hill_diagonals[depth + i] = False
                    dale_diagonals[depth - i] = False
                    path.pop()

        cols = [False] * n
        hill_diagonals = [False] * (2 * n - 1)  #主对角线差是定值
        dale_diagonals = [False] * (2 * n - 1)  #副对角线和是定值
        path = []
        res = []
        backtrack(0)
        return [["." * i + "Q" + "." * (n - i - 1) for i in path ] for path in res]


#这个分块写了，好理解一些。
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def could_place(row, col):
            return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])

        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            hill_diagonals[row - col] = 1
            dale_diagonals[row + col] = 1

        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0

        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)

        def backtrack(row=0):
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)

        cols = [0] * n
        hill_diagonals = [0] * (2 * n - 1)
        dale_diagonals = [0] * (2 * n - 1)
        queens = set()
        output = []
        backtrack()
        return output

