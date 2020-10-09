N = int(input())
for i in range(N):
    rows, cols = map(int, input().split())
    maze = []
    for i in range(rows):
        row_maze = []
        row = input().split()
        for j in range(cols):
            if row[j] == 'S': prince = (i,j)
            if row[j] == 'E': princess = (i,j)
            row_maze.append(row[j])
        maze.append(row_maze)
    print(maze,prince,princess)



dirs = [(0,1),(1,0),(0,-1),(-1,0)]
path = []
def mark(maze,pos):
    maze[pos[0]][pos[1]] = 2
def passable(maze,pos):
    if pos[0] >= rows and pos[1] >= cols:
        return False
    return maze[pos[0]][pos[1]] == '.'
def find_path(maze,pos,end):
    mark(maze,pos)
    if pos == end:
        print('YES')
        return True
    for i in range(4):
        nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
        if passable(maze,nextp):
            if find_path(maze,nextp,end):
                print('YES')
                return True
    print('NO')

    return False
find_path(maze,prince,princess)