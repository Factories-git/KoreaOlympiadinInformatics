#12점 받은 코드 (시간초과는 아님)
from math import log2 as log, ceil


n = int(input())
arr = list(map(int, input().split()))
c = 0
for i in range(1, n):
    if arr[i - 1] > arr[i]:
        lg = ceil(log(arr[i - 1]) / arr[i])
        arr[i] <<= lg
        c += lg
        print(lg)

print(c, arr)