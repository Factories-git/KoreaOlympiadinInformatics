n = int(input())
tower = list(map(int, input().split()))
stack = [n-2]
re = [0] * n
for i in range(n-1, 0, -1):
    pointer = i-1
    while tower[i] > tower[stack[-1]] or i == stack[-1]:
        stack.append(pointer)
        pointer -= 1
    re[i] = stack[-1]
for i in re:
    if i <= 0:
        print(0, end=' ')
        continue
    print(i+1, end=' ')