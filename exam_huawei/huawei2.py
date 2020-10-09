import copy
rows, cols = map(int, input().split())
# print(rows, cols,type(rows))
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
print(matrix)

def luoxuanSort(matrix):
    if not matrix: return []
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    x, y = 0 , 0

    line_list = []

    for num in matrix:
        line_list = line_list + num
    sorted(line_list)

    m,n  = len(matrix), len(matrix[0])

    di = 0
    visited = set()

    ans = copy.deepcopy(matrix)

    for i in range(m*n):
        ans[x][y] = line_list[i]
        visited.add((x,y))
        tx,ty = x + dx[di], y + dy[di]
        if 0 <= tx < m and a <= ty < n and (tx,ty) not in visited:
            x, y = tx, ty
        else:
            di = (di + 1) % 4
            x, y  = x + dx[di], y + dy[di]
    return ans

print(luoxuanSort(ans))
