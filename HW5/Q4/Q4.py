# string = "((()"
n = input()
string = input()
dp = [[0 for i in range  (len(string)+1)] for i in range (len(string)+1)]

for i in range(len(string) + 1):
    for j in range(0, i):
        dp[i][j] = 1

mod = 1000000009
for i in range(len(string)):
    for j in range(i, len(string)):
        if (j-i+1)%2 == 1:
            dp[i + 1][j + 1] = 0
            continue
        if j-1 >= 0 and string[j-1] == "(":
            dp[i+1][j+1] = (dp[i+1][j+1]+dp[i+1][j-1])%mod
        if string[i] == "(" and i+2 < j:
            dp[i+1][j+1] = (dp[i+1][j+1]+dp[i+2][j])%mod

print(dp[1][len(string)]%mod)