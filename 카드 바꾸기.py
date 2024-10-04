from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
increase = 0
decrease = 0
c = Counter(cards)
same = c[max(c.values())]
print(same)