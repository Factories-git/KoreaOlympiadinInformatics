#13점 나온 코드 (약 20%)
#작성중
"""
반례:
8
0 0 1 1 1 0 0 0
"""
# def compare():
#     c = rooms[k]
#     if rooms[k] == 0:
#         c = 1
#     y = rooms[i]
#     if y == 0:
#         y = 1
#     if dp[i - 1] + y >= dp[i - 1] + c:
#         dp[i] = dp[i - 1] + y
#         used[k] = True
#     else:
#         dp[i] = dp[i - 1]
#
#
#
# n = int(input())
# rooms = list(map(int, input().split()))
# used = [False] * n
# dp = [0] * n
# for i in range(n):
#     if used[i]:
#         dp[i] = dp[i-1]
#         continue
#     k = (i+1) % n
#     j = rooms[i]
#     if j != 0:
#         dp[i] = dp[i-1] + 1
#     else:
#         compare()
#     used[i] = True
# print(max(dp))

#밑은 21점 코드, 38%에서 틀림
#위의 반례를 통과하지 못 함
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
    p = rooms[k] + (1 if rooms[k] == 0 else 0)
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