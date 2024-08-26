n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

j = 0
cnt = 0

i = 0
while i < n and j < m:
    if b[j] >= a[i]:
        cnt += 1
        i += 1
    j += 1

ans = max(0, n - cnt)
print(ans)