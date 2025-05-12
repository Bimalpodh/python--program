def minimum_string_factor(X, Y, S, R):
    n = len(X)
    m = len(Y)
    Y_rev = Y[::-1]

    dp = [[float('inf')] * 2 for _ in range(n + 1)]
    dp[0][0] = dp[0][1] = 0

    for i in range(n):
        for j in range(1, m + 1):
            if i + j <= n and X[i:i + j] == Y[:j]:
                dp[i + j][0] = min(dp[i + j][0], dp[i][0] + 1)
        
        for j in range(1, m + 1):
            if i + j <= n and X[i:i + j] == Y_rev[:j]:
                dp[i + j][1] = min(dp[i + j][1], dp[i][1] + 1)

    min_substrings = min(dp[n][0], dp[n][1])

    if min_substrings == float('inf'):
        return "Impossible"
    
    num_from_Y = min(dp[n][0], dp[n][1]) if dp[n][0] <= dp[n][1] else dp[n][0]
    num_from_Y_rev = dp[n][1] if dp[n][0] > dp[n][1] else 0
    string_factor = num_from_Y * S + num_from_Y_rev * R

    return string_factor

X = input().strip()
Y = input().strip()
S, R = map(int, input().strip().split())

result = minimum_string_factor(X, Y, S, R)
print(result)







