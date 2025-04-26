n, k = map(int, input().split())
arr = list(map(int, input().split()))
new_arr = []
c = 0
for idx, i in enumerate(arr):
    new_arr.append([i, idx])
new_arr.sort()
for i in range(n-1, n-k-1, -1):
    p = new_arr[i][0]
    loc = new_arr[i][1]
    for j in range(n-1, n-k-1, -1):
        if loc == new_arr[j][1]: continue
        if loc > new_arr[j][1]:
            p -= 1
    c += p
print(c)