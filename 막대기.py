import sys

input = sys.stdin.readline

n = int(input())
stick = [int(input()) for i in range(n)]
stack = [stick[-1]]
for i in range(n-2, -1, -1):
    if stack[-1] < stick[i]:
        stack.append(stick[i])
print(len(stack))