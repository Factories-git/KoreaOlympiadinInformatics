n = int(input())
aqua = list(map(int, input().split()))
left = 0
right = n - 1
aqua.sort()
max_ = (aqua[left], aqua[right])

while left < right:
    current_sum = aqua[left] + aqua[right]
    if current_sum == 0:
        max_ = (aqua[left], aqua[right])
        break
    if abs(0 - current_sum) < abs(0 - (max_[0] + max_[1])):
        max_ = (aqua[left], aqua[right])
    if current_sum < 0:
        left += 1
    else:
        right -= 1

print(min(max_[0], max_[1]),max(max_[0], max_[1]))
