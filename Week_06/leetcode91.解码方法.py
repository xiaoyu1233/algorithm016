def numDecodings(s):

    n = len(s)
    dp = [0]*n #dp[i]表示s从下标[0]到[i]的方法总数
    dp[0] = 1 if s[0]!="0" else 0
    if n>=2:
        #为了方便理解初始化dp[1],也可初始化dp长度n+1来避免此步骤
        dp[1] = 1 if s[1]=="0" and  0<int(s[0])<=2 \
            else 0 if s[1]=="0" \
            else 2 if 10<int(s[0]+s[1])<=26 \
            else dp[0]
    for i in range(2,n):
        #先针对"0"字符中是否为10和20的情况进行判断
        #再判断11-26的情况
        #然后是其他1-9的情况
        dp[i] = dp[i-2] if s[i]=="0" and  0<int(s[i-1])<=2\
            else 0 if s[i]=="0" \
            else dp[i-2]+dp[i-1] if 10<int(s[i-1]+s[i])<=26 \
            else dp[i-1]
    # print(dp)
    return dp[-1]

