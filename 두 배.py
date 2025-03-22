#런타임 에러(33점)
from math import log2 as log, ceil

n = int(input())
arr = list(map(int, input().split()))
c = 0
remember = arr[0]
for i in range(1, n):
    if remember > arr[i]:
        lg = ceil(log(remember / arr[i]))
        remember = arr[i] << lg
        c += lg
    else:
        remember = arr[i]

print(c)