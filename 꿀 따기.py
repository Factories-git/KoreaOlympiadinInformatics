n = int(input())
honey = list(map(int, input().split()))
s = [honey[0]]

for i in range(1, n):
    s.append(honey[i] + s[-1]) #구간 합 구하기

honey0 = 0
for i in range(1, n): #벌 벌 꿀통 케이스 처리
    x = s[-1]
    honey0 = max(honey0, 2 * x - honey[0] - honey[i] - s[i])
    #왼쪽 벌은 s[-01] - honey[0] - honey[i]만큼 따고, 움직이는 벌은 s[-1] - s[i] 만큼 땀.

honey1 = 0
for i in range(1, n-1): # 꿀통 벌 벌 케이스 처리
    x = s[-1]
    honey1 = max(honey1, (s[-1] - honey[-1] - honey[i]) + (s[i-1]))
    #오른쪽 벌은 s[-1] - honey[-1] - honey[i] 만큼 따고, 움직이는 벌은 s[i-1]만큼 땀.
honey2 = 0
for i in range(1, n-1): # 벌 꿀통 벌 케이스 처리
    honey2 = max(honey2, (s[i] - honey[0]) + (s[-1] - honey[-1] - s[i-1]))
    # 왼쪽 벌은 s[i] - honey[0], 오른쪽 벌은 s[-1] - honey[-1] - s[i-1] 만큼 딸 수 있음.
print(max(honey0, honey1, honey2)) #정답 반환