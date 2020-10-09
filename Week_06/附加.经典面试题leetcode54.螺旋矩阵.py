#zip还能这么用，nice

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res

#方向数组的使用，妙啊
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:return []
        m,n = len(matrix),len(matrix[0])
        x = y = di = 0
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        res = []
        visited = set()

        for i in range(m*n):
            res.append(matrix[x][y])
            visited.add((x,y))
            nx,ny = x+dx[di],y+dy[di]
            if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited:
                x,y = nx,ny   
            else:
                di = (di+1)%4  # 如果不满足条件，换一个方向进行遍历
                x,y = x+dx[di],y+dy[di]
        return res



class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        NROW = len(matrix)
        NCOL = len(matrix[0])

        def helper(depth):
            nrow, ncol = NROW - 2 * depth, NCOL - 2 * depth
            if nrow <= 0 or ncol <= 0: return []
            if nrow == 1: return matrix[depth][depth:depth + ncol]
            if ncol == 1: return [matrix[r][depth] for r in range(depth, depth + nrow)]

            res = []
            res += matrix[depth][depth:depth + ncol - 1]
            res += [matrix[r][depth + ncol - 1] for r in range(depth, depth + nrow - 1)]
            res += reversed(matrix[depth + nrow - 1][depth + 1:depth + ncol])
            res += [matrix[r][depth] for r in reversed(range(depth + 1, depth + nrow))]
            return res + helper(depth + 1)

        return helper(0)


作者：hzhu212
链接：https: // leetcode - cn.com / problems / spiral - matrix / solution / yi - chong - you - ya - de - bian - li - fang - shi - dai - ma - zheng - q /
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。