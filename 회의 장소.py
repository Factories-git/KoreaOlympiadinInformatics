import sys

input = sys.stdin.readline
print = sys.stdout.write


def bisect_lower(target):
    left, right = 0, n - 1
    res = -1  # 못 찾는 경우 -1
    while left <= right:
        mid = (left + right) // 2
        if houses[mid] > target:
            right = mid - 1
        else:
            res = mid
            left = mid + 1
    return res

def bisect_upper(target):
    left, right = 0, n - 1
    res = n  # 못 찾는 경우를 대비해 배열 크기 N으로 초기화
    while left <= right:
        mid = (left + right) // 2
        if houses[mid] >= target:
            res = mid  # 조건을 만족하면 결과를 저장하고
            right = mid - 1  # 왼쪽 절반을 다시 탐색
        else:
            left = mid + 1  # 조건을 만족하지 않으면 오른쪽 탐색
    return res

def get_val(tar, left, right):
    val1 = prefix_sum[right+1] - prefix_sum[tar] - houses[tar] * (right - tar + 1)
    val2 = houses[tar] * (tar - left + 1) - (prefix_sum[tar+1] - prefix_sum[left])
    return val2 + val1


n, q = map(int, input().split())
houses = list(map(int, input().split()))
prefix_sum = [0]
for i in houses:
    prefix_sum.append(prefix_sum[-1] + i)
for i in range(q):
    L, R = map(int, input().split())
    l = bisect_upper(L)
    r = bisect_lower(R)
    if l > r:
        print('0\n')
        continue

    v1 = get_val(l, l, r)
    v2 = get_val(r, l, r)
    v3 = get_val((l + r) // 2, l, r)

    print(f'{max(v1, v2) - v3}\n')