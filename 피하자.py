n = int(input())
arr = list(map(int, input().split()))
odd = 0
even = 0
c_1 = 0
c_2 = 0
for i in range(n):
    if arr[i] % 2:
        odd += 1
        c_1 += even
    else:
        even += 1
        c_2 += odd
print(min(c_1, c_2))