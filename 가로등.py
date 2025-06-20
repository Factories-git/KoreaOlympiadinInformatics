from collections import deque

l, n, k = map(int, input().split())
streetlights = list(map(int, input().split()))


def bfs(lights):
    s = {}
    queue = deque()
    n_k = 0
    visited = set()
    for i in lights:
        queue.append(i)
        visited.add(i)
        s[i] = 0
        n_k += 1
    while queue:
        location = queue.popleft()
        for i in [-1, 1]:
            nl = location + i
            if nl < 0 or nl > l or nl in visited:
                continue
            s[nl] = s[location] + 1
            visited.add(nl)
            queue.append(nl)
            n_k += 1
        if n_k >= k:
            break

    result = []
    for _, darkness in s.items():
        result.append(darkness)
    return sorted(result)


for i in bfs(lights=streetlights)[:k]:
    print(i)