def count_differ(arr): #차이 찾는 함수
    c = 0
    for i in range(n):
        for j in range(len(arr[i])):
            if arr[i][j] != arr2[i][j]: c+=1
    return c


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]
c = float('inf')

for _ in range(3): #3번 회전 (원상 복귀까지)
    arr_n = [[0] * (i+1) for i in range(n)] #리스트 선언(임시)
    for i in range(n):
        for j in range(i+1):
            arr_n[i][j] = arr[n - 1 - i + j][n - 1 - i] #규칙에 따라 변환
    c = min(c, count_differ(arr_n)) #차이 찾고 갱신
    arr = arr_n

arr_n = [[0] * (i+1) for i in range(n)] #리스트 선언(임시)
for i in range(n): #뒤집기
    for j in range(i+1):
        arr_n[i][j] = arr[i][i - j] #규칙에 따라 뒤집기
c = min(c, count_differ(arr_n))
arr = arr_n

for _ in range(3): #뒤집은 상태로 다시 회전 [이하 로직 같음]
    arr_n = [[0] * (i+1) for i in range(n)]
    for i in range(n):
        for j in range(i+1):
            arr_n[i][j] = arr[n - 1 - i + j][n - 1 - i]
    c = min(c, count_differ(arr_n))
    arr = arr_n

print(c)