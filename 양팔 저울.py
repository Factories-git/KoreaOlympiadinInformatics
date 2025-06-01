k = int(input())
weight = list(map(int, input().split()))
s = sum(weight)
result = [False] * (s + 1)
def backtracking(idx, total):
    if total > s:
        return
    if idx == k:
        if 0 < total <= s:
            result[total] = True
    else:
        backtracking(idx + 1, total)
        backtracking(idx + 1, total - weight[idx])
        backtracking(idx + 1, total + weight[idx])



backtracking(0, 0)
print(result.count(False) - 1)