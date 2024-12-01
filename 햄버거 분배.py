n,k = map(int, input().split())
s = list(input())
c = 0

for i in range(n):
    if s[i] != 'P':
        continue
    for j in range(i-k,i+k+1):
        if j < 0 or j >= n:
            continue
        if s[j] == 'H':
            s[j] = '-'
            c += 1
            break
print(c)