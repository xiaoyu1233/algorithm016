while True:
    first_line = list(map(int, input().split()))
    M = first_line[0]
    N = first_line[1]
    matrix = []
    for i in range(M):
        other_line = list(input().split())
        row = []
        for ch in other_line[0]:
            row.append(ch)
        matrix.append(row)
    #print(matrix)
    #print(matrix[0][1])

    def maxSquare(matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        bian_length = 0
        rows, cols = len(matrix), len(matrix[0])

        dp = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 'M':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],dp[i - 1][j - 1]) + 1
                    bian_length = max(bian_length,dp[i][j])
        #print(dp)

        res = bian_length * bian_length
        print(res)
    maxSquare(matrix)

        #print(other_line)
        #for j in range(N):
