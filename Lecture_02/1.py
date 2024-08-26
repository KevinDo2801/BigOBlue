a = list(map(int, input().split()))
n = a[0]
k = a[1]

a = list(map(int, input().split()))

temp = 0
l = 0
s = {}

for i in range(0, n):
    if a[i] not in s:
        temp += 1
        s[a[i]] = 1
    else:
        s[a[i]] += 1
    if temp == k:
        while s[a[l]] != 1:
            s[a[l]] -= 1
            l += 1
        print(l + 1, i + 1)
        exit()

print(-1, -1)

