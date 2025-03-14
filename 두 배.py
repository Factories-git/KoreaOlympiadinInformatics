#33점 받은 코드

n = int(input())
arr = list(map(int, input().split()))
c = 0
for i in range(1, n):
    if arr[i-1] > arr[i]:
        k = 0
        while arr[i-1] > arr[i]:
            arr[i] *= 2
            c += 1
            k += 1
print(c)