from itertools import combinations

n,k = map(int, input().split())
houses = []
for i in range(n):
    houses.append(list(map(int, input().split())))

nCk = list(combinations(houses, k))
answer = float('inf')

for shelters in nCk:
    max_dis = 0

    for house in houses:
        min_dis = float('inf')
        for shelter in shelters:
            dis = abs(shelter[0] - house[0]) + abs(shelter[1] - house[1])
            min_dis = min(min_dis, dis)
        max_dis = max(min_dis, max_dis)
    answer = min(answer, max_dis)

print(answer)
# n,k = map(int, input().split())
# houses = []
# for i in range(n):
#     houses.append(list(map(int, input().split())))
#
# distances = [[float('inf')] * n for i in range(k)]
# shelters = []
# for _ in range(k):
#     for i in range(n):
#         shelter = houses[i]
#         for j in range(n):
#             distance =
#             if distance != 0:
#                 distances[_][j] = min(distance, distances[_][j])
#         print(distances)
# maxes = []
# for i in distances:
#     maxes.append(max(i))
#     print(i, max(i))
# print(min(maxes))