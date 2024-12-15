import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def dfs(y, x):
    global count
    if y < 0 or y >= n or x < 0 or x >= n:
        return False
    if map_[y][x] == 1:
        map_[y][x] = 0
        count += 1
        dfs(y + 1, x)
        dfs(y - 1, x)
        dfs(y, x + 1)
        dfs(y, x - 1)
        return True
    return False


n = int(input())
count = 0
map_ = []
counts = []
re = 0
for i in range(n):
    map_.append(list(map(int, input().strip())))
for i in range(n):
    for j in range(n):
        result = dfs(i, j)
        if result:
            counts.append(count)
            re += 1
            count = 0
print(re)
counts.sort()
for i in counts:
    print(i)