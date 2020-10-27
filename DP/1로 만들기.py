from collections import defaultdict
N = int(input())

dp = defaultdict(int)

def make(n):
     if n in [1,2,3,5]:
         return 1

     if dp[n]:
         return dp[n]

     dp[n] = make(n-1)+1
     for i in [2, 3, 5]:
         if n % i == 0:
             dp[n] = min(dp[n], make(n // i) + 1)
     return dp[n]

print(make(N))

