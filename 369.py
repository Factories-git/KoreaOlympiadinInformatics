n = int(input())
c = 0
for i in range(1, n+1):
    c += str(i).count('3')
    c += str(i).count('6')
    c += str(i).count('9')
print(c)