from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
increase = 0
decrease = 0
for i in range(1,n):
    if cards[i-1] + 1 != cards[i]:
        cards[i] = cards[i-1]+1
        increase += 1