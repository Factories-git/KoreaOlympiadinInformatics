
n, k = map(int, input().split())
countries = []
for i in range(n):
    country, gold, silver, bronze = map(int, input().split())
    countries.append([gold, silver, bronze, country])
countries.sort(reverse=True)
prize = []
for i in range(n):
    if i > 0:
        if countries[i-1][:3] == countries[i][:3]:
            prize.append([prize[-1][0], countries[i]])
        else:
            prize.append([i+1, countries[i]])
    else:
        prize.append([i+1, countries[i]])
for i in prize:
    if i[1][-1] == k:
        print(i[0])