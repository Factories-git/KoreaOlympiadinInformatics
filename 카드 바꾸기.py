from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
c = Counter(cards)
increase = n
decrease = n
same = 0
m_k = 0
max_ = max(c.values())
for k, v in c.items():
    if v == max_:
        m_k = k
for i in cards:
    if i != m_k:
        same += 1

for i in range(1, n):
    new_card = cards.copy()
    new_s = 0
    diff = cards[i-1] - cards[i]
    if diff == 0:
        continue
    for j in range(n-1, 0, -1):
        if diff == new_card[j-1] - new_card[j]:
            continue
        new_card[j] = new_card[j-1] - diff
        new_s += 1

    if new_card[0] - new_card[1] != diff:
        new_card[0] = new_card[0] - diff
        new_s += 1
    decrease = min(new_s, decrease)

for i in range(1, n):
    new_card = cards.copy()
    new_s = 0
    diff = cards[i-1] - cards[i]
    if diff == 0:
        continue
    if new_card[0] - new_card[1] != diff:
        new_card[0] = new_card[0] - diff
        new_s += 1
    for j in range(1, n):
        if diff == new_card[j-1] - new_card[j]:
            continue
        new_card[j] = new_card[j-1] - diff
        new_s += 1
    increase = min(new_s, increase)
print(min(increase, decrease, same))