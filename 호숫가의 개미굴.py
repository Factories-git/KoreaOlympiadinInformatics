#21점 나온 코드

n = int(input())
rooms = list(map(int, input().split()))
c = 0
used = [False] * n
dp = [0] * n
for i in range(n):
    if used[i]:
        dp[i] = dp[i-1]
        continue
    k = (i+1) % n
    j = rooms[i]
    if j != 0:
        dp[i] = dp[i-1] + j
    else:
        if rooms[k] == 0:
            used[k] = True
            if i == 0 and used[-1] == 0:
                used[-1] = True
        dp[i] = dp[i-1] + 1
    used[i] = True
print(max(dp))