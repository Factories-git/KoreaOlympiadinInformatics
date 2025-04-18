n = int(input())
honey = list(map(int, input().split()))
a1 = [0]
for i in range(n):
    a1.append(a1[i] + honey[i])
a1.pop(0)
honey0 = -1
for i in range(1, n):
    k = (a1[-1] - a1[i]) * 2
    k += a1[i] - a1[0] - honey[i]
    honey0 = max(honey0, k)
honey1 = 0
for i in range(1, n-1):
    k = a1[i] - honey[0]
    s = a1[-1] - honey[0] - honey[-1]
    honey1 = max(honey1, k+s)

honey2 = 0
for i in range(n-1, 1, -1):
    k = (a1[i-1] - a1[0]) * 2
    k += a1[-1] - a1[i]
    honey2 = max(honey2, k)
print(max([honey0, honey1, honey2]))