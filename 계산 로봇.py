import sys

input = sys.stdin.readline


m, n = map(int, input().split())
D = [list(map(int, input().strip())) for i in range(m)] #weight
save = [[0] * n for _ in range(m)]
output = [[0] * n for _ in range(m)]

for i in range(m):
    output[i][0] = D[i][0]

answer = 0
for j in range(1, n): #행에 대한 반복
    for i in range(m): #열에 대한 반복
        #현재 저장값 = 이전 출력 값
        save[i][j] = output[i][j-1]
        if i > 0:
            save[i][j] = max(save[i][j], output[i-1][j-1])
        if i < m - 1:
            save[i][j] = max(save[i][j], output[i+1][j-1])
        output[i][j] = save[i][j] + D[i][j]
        answer = max(save[i][j], answer)

print(answer)