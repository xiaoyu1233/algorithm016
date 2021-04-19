import sys
lines = int(input())
for n in range(1,lines+1):
    a = input().split()
    c = sum(int(a[i]) for i in range(1,int(a[0])+1))
    print(c)

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



# import sys
# matirx = []
# for line in sys.stdin:
#     a = line.split()
#     #print(a)
#     matirx.append(a)
#     print(',',matirx)


num = int(input())
#print(num)
for i in range(num):
    #row = input()
    row = list(input().split())
    max_zimu = max(row[0])
    idx = row[0].index(max_zimu)
    temp1 = row[0][0]
    temp2 = row[0][idx]
    s = temp2+ row[0][0:idx] + temp1+row[0][idx + 1:]
    print(s)

l = max(len(row[0]), len(row[1]))
flag = True
for i in range(len(row[0])):
    #for j in range(len(row[1])):
    if row[0][i] > row[1][i]:
        continue
    for j in range(i + 1, len(row[0])):
        if row[0][j] > row[1][i]:
            row[0] = row[0][j] + row[0][i + 1:idx] + row[0][i]+row[0][idx + 1:]
        else:
            flag = False
if flag == True:
    print(row[0])
else:
    print(row[1])