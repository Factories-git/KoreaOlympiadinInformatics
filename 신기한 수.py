n = int(input())
c = 0
for i in range(1, n+1):
    s = 0
    for j in range(len(str(i))):
        s += int(str(i)[j])
    if i % s == 0:
        c += 1
print(c)