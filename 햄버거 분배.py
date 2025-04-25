n, k = map(int, input().split())
hamburger = list(input())
visit = [False] * n
c = 0
for i in range(n): #반복
    if hamburger[i] == 'H': continue #햄버거가 사람을 먹을 수는 없음
    for j in range(i - k, i + k + 1): #사람을 기준으로 왼쪽과 오른쪽 살핌
        if j < 0 or j >= n: # 범위 벗어난것은 카운트 안함
            continue
        if visit[j] or hamburger[j] == 'P': #이미 먹었거나 사람이면 넘어감
            continue
        visit[j] = True #방문처리
        c += 1 #정답 변수 + 1
        break
print(c)