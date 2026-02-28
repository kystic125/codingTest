def dp(lst, n):
      
    dp = []
    for i in range(2):
        dp.append([0] * n)

    dp[0][0] = lst[0][0]
    dp[1][0] = lst[1][0]

    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1], dp[1][i-1] + lst[0][i])
        dp[1][i] = max(dp[1][i-1], dp[0][i-1] + lst[1][i])
                       
    m = 0

    for i in dp:
        if i[-1] > m:
            m = i[-1]

    return m

t = int(input())

for i in range(t):
    n = int(input())
    lst = []
    for i in range(2):
        lst.append(list(map(int, input().split())))
    print(dp(lst, n))
