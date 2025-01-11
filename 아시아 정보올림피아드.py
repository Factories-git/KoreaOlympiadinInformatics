scores = []
countries = {}
test = int(input())
for i in range(test):
    c,n,p = map(int, input().split())
    scores.append([c,n,p])
    countries[c] = 0
scores.sort(key=lambda x:-x[2])
gold = 0
silver = 0
bronze = 0
for i in range(len(scores)):
    t = scores[i]
    c = t[0]
    n = t[1]
    s = t[2]
    if i == 0:
        gold = (c, n)
        countries[c] += 1
        continue
    elif i == 1:
        silver = (c, n)
        countries[c] += 1
        continue
    if countries[c] >= 2:
        continue
    bronze = (c, n)
    break
print(gold)
print(silver)
print(bronze)
