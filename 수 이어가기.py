import random

max_ = 0
n = int(input())
chosen = []
for choose in range(30000):
    chose = [n, choose]
    pointer = 2
    while True:
        if chose[pointer - 2] - chose[pointer - 1] < 0:
            break
        chose.append(chose[pointer - 2] - chose[pointer - 1])
        pointer += 1
    max_ = max(max_, len(chose))
    chosen.append(chose)

print(max_)
for i in chosen:
    if len(i) == max_:
        print(*i)
        break
