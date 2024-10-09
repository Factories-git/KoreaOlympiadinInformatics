import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def dfs(x, y):
    if x < 0 or x >= t or y < 0 or y >= t:
        return False
    if farm[x][y] == 1:
        farm[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True

    return False


t = int(input())
re = 0
farm = []
for s in range(t):
    farm.append(list(map(int, input().split())))
for i in range(t):
    for j in range(t):
        if dfs(i, j):
            re += 1
    print(re)
    re = 0
