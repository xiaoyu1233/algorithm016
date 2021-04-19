num = int(input())
#print(num)
for i in range(num):
    #row = input()
    row = list(input().split())
    # max_zimu = max(row[0])
    # idx = row[0].index(max_zimu)
    # temp1 = row[0][0]
    # temp2 = row[0][idx]
    # s = temp2+ row[0][0:idx] + temp1+row[0][idx + 1:]
    # print(s)

    l = min(len(row[0]), len(row[1]))
    flag = True
    for i in range(len(row[0])):
        #for j in range(len(row[1])):
        if row[0][i] > row[1][i]:
            continue
        for j in range(i + 1, len(row[0])):
            if row[0][j] > row[1][i]:
                row[0] = row[0][j] + row[0][i + 1:j] + row[0][i]+row[0][j + 1:]
            else:
                flag = False
    if flag == True:
        print(row[0])
    else:
        print(row[1])