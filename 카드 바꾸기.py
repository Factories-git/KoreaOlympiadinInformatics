from collections import Counter

n = int(input())
cards = [0] + list(map(int, input().split()))
counter = {}
decrease = n
increase = n
same = 0
for i in range(1, len(cards)):
    for j in range(1, len(cards)):
        if cards[i] != cards[j]:
            same += 1
#증가하는 순서대로 카드 바꾸기
for i in range(1, len(cards)):
    new_card = cards.copy()
    new_s = 0
    diff = cards[i] - cards[i-1]
    if diff == 0:
        continue
    for j in range(2, len(cards)):
        if new_card[j] - new_card[j-1] == diff:
            continue
        new_card[j] = new_card[j-1] + diff
        new_s += 1
    if new_card[2] - new_card[1] != diff:
        new_card[1] = new_card[2] - diff
        new_s += 1
    increase = min(new_s, increase)
    print(new_card, diff, new_s, i)
#감소하는 순서대로
for i in range(1, len(cards)):
    new_card = cards.copy()
    new_s = 0
    diff = cards[i] - cards[i-1]
    if diff == 0:
        continue
    if new_card[len(cards) - 1] - new_card[len(cards) - 2] != diff:
        new_card[len(cards) - 1] = new_card[len(cards) - 2] + diff
        new_s += 1
    for j in range(len(new_card)-2, 0, -1):
        if new_card[j+1] - new_card[j] == diff:
            continue
        new_card[j] = new_card[j+1] - diff
        new_s += 1
    decrease = min(new_s, decrease)
print(min(increase, decrease, same))