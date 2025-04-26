n = int(input())
time = float('inf')
for i in range(n):
    a, b = map(int, input().split())
    if a > b: continue
    time = min(time, b)
print(time if time != float('inf') else -1)