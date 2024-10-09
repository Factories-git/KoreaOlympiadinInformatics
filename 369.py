n = int(input())
c = 0
for i in range(3, n+1):
    s = str(i)
    c += s.count('3')
    c += s.count('6')
    c += s.count('9')
print(c)