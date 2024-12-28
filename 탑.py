n = int(input())
tower = list(map(int, input().split()))
re = [0] * n
stack = []
for i in range(n-1, -1, -1):
    if stack:
        while stack[-1][0] <= tower[i]:
            stack.pop()
            if not stack:
                break
    if stack:
        re[i] = stack[-1][1]
    stack.append([tower[i], i])
    print(stack, i)
for i in re:
    if i <= 0:
        print(0, end=' ')
        continue
    print(i+1, end=' ')