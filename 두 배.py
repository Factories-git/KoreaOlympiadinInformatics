from math import log2 as log, ceil

n = int(input())
arr = list(map(int, input().split()))
c = 0
remember = 0
for i in range(1, n):
    lg = ceil(log(arr[i-1] / arr[i])) + remember
    if 0 < lg:
        remember = lg
        c += lg
    else:
        remember = 0
print(c)