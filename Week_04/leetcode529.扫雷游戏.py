#DFS
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i, j = click
        row, col = len(board), len(board[0])
        if board[i][j] == "M":
            board[i][j] = "X"
            return board

        # 计算空白快周围的***
        def cal(i, j):
            res = 0
            for x in [1, -1, 0]:
                for y in [1, -1, 0]:
                    if x == 0 and y == 0: continue
                    if 0 <= i + x < row and 0 <= j + y < col and board[i + x][j + y] == "M": res += 1
            return res

        def dfs(i, j):
            num = cal(i, j)
            if num > 0:
                board[i][j] = str(num)
                return
            board[i][j] = "B"
            for x in [1, -1, 0]:
                for y in [1, -1, 0]:
                    if x == 0 and y == 0: continue
                    nxt_i, nxt_j = i + x, j + y
                    if 0 <= nxt_i < row and 0 <= nxt_j < col and board[nxt_i][nxt_j] == "E": dfs(nxt_i, nxt_j)

        dfs(i, j)
        return board

#BFS
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i, j = click
        row, col = len(board), len(board[0])
        if board[i][j] == "M":
            board[i][j] = "X"
            return board

        # 计算空白快周围的***
        def cal(i, j):
            res = 0
            for x in [1, -1, 0]:
                for y in [1, -1, 0]:
                    if x == 0 and y == 0: continue
                    if 0 <= i + x < row and 0 <= j + y < col and board[i + x][j + y] == "M": res += 1
            return res

        def bfs(i, j):
            queue = collections.deque([[i, j]])
            while queue:
                i, j = queue.pop()
                num = cal(i, j)
                if num > 0:
                    board[i][j] = str(num)
                    continue
                board[i][j] = "B"
                for x in [1, -1, 0]:
                    for y in [1, -1, 0]:
                        if x == 0 and y == 0: continue
                        nxt_i, nxt_j = i + x, j + y
                        if nxt_i < 0 or nxt_i >= row or nxt_j < 0 or nxt_j >= col: continue
                        if board[nxt_i][nxt_j] == "E":
                            queue.appendleft([nxt_i, nxt_j])
                            board[nxt_i][nxt_j] = "B"

        bfs(i, j)
        return board

