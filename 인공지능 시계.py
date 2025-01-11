h, m, s = map(int, input().split())
d = int(input())
if d >= 60:
    m1, s1 = divmod(d, 60)
    m += m1
    s += s1
else:
    s += d
if s >= 60:
    m += s // 60
    s %= 60
if m >= 60:
    h += m // 60
    m %= 60
if h >= 24:
    h %= 24

print(h, m, s)