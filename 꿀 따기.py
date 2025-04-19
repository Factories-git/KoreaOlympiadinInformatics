n = int(input())
honey = list(map(int, input().split()))
s = [honey[0]]

for i in range(1, n):
    s.append(honey[i] + s[-1])

honey0 = 0
for i in range(1, n):
    x = s[-1]
    honey0 = max(honey0, 2 * x - honey[0] - honey[i] - s[i])

honey1 = 0
for i in range(1, n-1):
    x = s[-1]
    honey1 = max(honey1, (s[-1] - honey[-1] - honey[i]) + (s[i-1]))
honey2 = 0
for i in range(1, n-1):
    honey2 = max(honey2, (s[i] - honey[0]) + (s[-1] - honey[-1] - s[i-1]))
print(max(honey0, honey1, honey2))