string = "((((()))())))()((())((()))(()"
n = len(string)
dp = [[0 for i in range(n)] for i in range(n + 1)]

dp[0][0] = 1

module = pow(10, 9) + 9
for i in range(1, n + 1):
    if string[i - 1] == ")":
        for j in range(n - 1):
            dp[i][j] = dp[i - 1][j + 1] % module
        dp[i][n - 1] = 0
    elif string[i - 1] == "(":
        for j in range(1, n - 1):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % module
        dp[i][0] = (dp[i - 1][1] % module) if n >= 2 else 0
        dp[i][n - 1] = dp[i - 1][n - 2] % module

print(dp[n][0] % module)