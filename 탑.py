n = int(input())
tower = list(map(int, input().split()))
re = [0] * n
stack = [i for i in range(n-1)]
for i in range(n-1, 0, -1):
    while tower[stack[-1]] < tower[i] or i == stack[-1]:
        try:
            stack.pop()
            re[i] = stack[-1]
        except IndexError:
            break
    if stack:
        re[i] = stack[-1]
for i in re:
    if i <= 0:
        print(0, end=' ')
        continueㄴㅇㄹ
    print(i+1, end=' ')