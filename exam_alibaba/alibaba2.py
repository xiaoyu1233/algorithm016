while True:
    first_line = list(map(int, input().split()))
    n = first_line[0]
    m = first_line[1]
    matrix = []
    for i in range(m):
        other_line = list(map(int, input().split()))
        # row = []
        # for ch in other_line[0]:
        #     row.append(ch)
        matrix.append(other_line)
    out_list = [0] * (n + 1)
    in_list = [0] * (n + 1)
    maxValue = -1
    minValue = -1
    maxcnt = 0
    mincnt = 0
    #计算入度和出度
    for idx, edge in enumerate(matrix):
        out_list[edge[1]] = out_list[edge[1]] + 1
        in_list[edge[0]] = in_list[edge[0]] + 1
    for idx in range(1, n + 1):
        if out_list[idx] == 0:
            mincnt += 1
            minValue = idx
        if in_list[idx] == 0:
            maxcnt += 1
            maxValue = idx

    if mincnt != 1:
        minValue = -1
    if maxcnt != 1:
        maxValue = -1
    print(minValue,maxValue)







    #print(matrix)
# import sys
# matirx = []
# for line in sys.stdin:
#     a = line.split()
#     #print(a)
#     matirx.append(a)
#     print(',',matirx)
