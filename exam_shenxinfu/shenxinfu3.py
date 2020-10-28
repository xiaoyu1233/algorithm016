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
    dp_s = [0] * (len(log_txt) + 1)
    dp_w = [0] * (len(log_txt) + 1)
    dp_r = [0] * (len(log_txt) + 2)
    count = 0
    #dp = [0] * (len(log_txt))
    for i in range(1, len(log_txt) + 1):
        dp_s[i] = dp_s[i - 1]
        if log_txt[i - 1] == 's':
            dp_s[i] += 1
        if log_txt[i - 1] == 'w':
            dp_w[i] = 1
        dp_r[len(log_txt) - i + 1] = dp_r[len(log_txt) - i + 2]
        if log_txt[len(log_txt) - i] == 'r':
            dp_r[len(log_txt) - i + 1] += 1
    for i in range(1,len(log_txt) + 1):
        if dp_w[i] == 1:
            count += dp_r[i] * dp_s[i]
    count = count % 1000000007
    #print(count, dp_s, dp_w, dp_r)
    print(count)





