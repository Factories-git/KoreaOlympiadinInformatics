n = int(input())
oil = list(map(int, input().split()))
money = list(map(int, input().split()))[:-1]
if all(num == money[0] for num in money):
    print(sum(oil) * money[0])
    exit(0)
c = money[0]
re = 0
for i in range(n-1):
    if c > money[i]:
        c = money[i]
    re += (c * oil[i])
print(re)
