import sys
from copy import deepcopy as copy

sys.setrecursionlimit(10 ** 6)

n = int(input())
p, f, s, v = map(int, input().split())
ingredients = [list(map(int, input().split())) for _ in range(n)]
re_price = float('inf')
re = []
ans = [0, 0, 0, 0, []]


def backtracking(depth, price):
    global re, re_price, ans

    if ans[0] >= p and ans[1] >= f and ans[2] >= s and ans[3] >= v:
        if re_price > price:
            re_price = price
            re = [(price, sorted(ans[-1]))]
        elif re_price == price:
            re.append((price, sorted(ans[-1])))
        return
    if depth == n:
        return

    for idx in range(depth, n):
        k = ingredients[idx]
        for i in range(4):
            ans[i] += k[i]
        ans[-1].append(idx)
        price += k[-1]

        backtracking(idx + 1, price)

        price -= k[-1]
        for i in range(4):
            ans[i] -= k[i]
        ans[-1].pop()


backtracking(0, 0)
if not re:
    print(-1)
    exit()
re.sort()
print(re_price)
for i in re[0][1]:
    print(int(i) + 1, end=' ')
