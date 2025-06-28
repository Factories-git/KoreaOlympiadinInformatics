n = int(input())
big = [list(map(int, input().split())) for _ in range(n)]
result = [0] * n
for i in range(n):
    k = 0
    my_height, my_kg = big[i]
    for j in range(n):
        height, kg = big[j]
        if j == i:
            continue
        if my_height < height and my_kg < kg:
            k += 1
    result[i] = k + 1
print(*result)