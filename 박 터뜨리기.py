n, k = map(int, input().split())
add = 0
for i in range(1, k+1):
    add += i
n -= add
if n < 0:
    print(-1)
elif n % k == 0:
    print(k-1)
else:
    print(k)