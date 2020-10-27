from collections import defaultdict

dp = defaultdict(int)

def findMin(t, money):
    if t <= 0:
        return -1

    if dp[t]:
        return dp[t]

    dp[t] = 10001
    for m in money:
        result = findMin(t-m, money)
        if result != -1:
            dp[t] = min(dp[t], findMin(t-m, money) + 1);

    if dp[t] == 10001:
        return -1
    return dp[t]

N, M = map(int, input().split())
money = []

for _ in range(N):
    k = int(input())
    money.append(k)
    dp[k] = 1

print(findMin(M, money))