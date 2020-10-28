# import copy
# rows, cols = map(int, input().split())
# # print(rows, cols,type(rows))
# matrix = []
# for i in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)


lines = int(input())
for line in range(lines):
    log_txt = input()
    count_s = 0
    count_w = 0
    count_r = 0
    count = 0
    i = 0
    while i < len(log_txt):
        while i < len(log_txt) and log_txt[i] != 'w':
            if log_txt[i] == 's':
                count_s += 1
            i += 1
        if count_s == 0:
            i += 1
            continue
        while i < len(log_txt) and log_txt[i] != 'r' :
            if log_txt[i] == 'w':
                count_w += 1
            i += 1
        if count_w == 0:
            i += 1
            continue
        while i < len(log_txt) and log_txt[i] != 's':
            if log_txt[i] == 'r':
                count_r += 1
            i += 1
        if count_r == 0:
            i += 1
            continue
        count += count_s * count_w * count_r
        #print(count_s, count_w, count_r)
        count_w = 0
        count_r = 0
    count = count % 1000000007
    print(count)

r[i] = [0]

for i in range(l):
    if


