rows, cols = map(int, input().split())
# print(rows, cols,type(rows))
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
# print(matrix)
res = []
# print(res)
for i in range(rows):
    res.append([])
# print(res)

numbers = rows * cols
visited = [[0] * cols for _ in range(rows)]
direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
temp = [0] * numbers

row_i, col_j = 0, 0
direct_m = 0
for i in range(rows):
    for j in range(cols):
        res[row_i][col_j] = matrix[i][j]
        print(res[row_i][col_j])
        nexRow, nexCol = row_i + direct[direct_m][0], col_j + direct[direct_m][1]
        if not (0 <= nexRow <= rows and 0 <= 0 <= nexCol <= cols):
            direct_m = (direct_m + 1) % 4
            row_i += direct[direct_m][0]
            col_j += direct[direct_m][1]
print(res)

# for j in range(cols):

