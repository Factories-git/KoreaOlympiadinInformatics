n = int(input())
s = input()
print(min(s.lstrip('R').count('R'), s.lstrip('B').count('B'), s.rstrip('R').count('R'), s.rstrip('B').count('B')))