n = int(input())
tower = list(map(int, input().split()))
re = [0] * n
new = [[j, i] for i, j in enumerate(tower)]
stack = []
for i in range(n):
    while stack:
        if stack[-1][0] <= new[i][0]:
            stack.pop()
        else:
            re[i] = stack[-1][1]+1
            break
    stack.append(new[i])
print(*re)