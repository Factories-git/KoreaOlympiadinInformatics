n = int(input())
arr = list(map(int, input().split()))
empty = [True] * n
ants = 0
for i in range(n):
    if arr[i]:
        ants += arr[i]
        continue
    if empty[i-1] and empty[(i+1) % n]:
        ants += 1
        empty[i] = False
print(ants)