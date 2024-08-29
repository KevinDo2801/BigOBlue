n = int(input())
a = list(map(int, input().split()))

l = 0
r = n - 1
s = 0
d = 0
flag = 0
while l <= r:
    if a[l] >= a[r]:
        if flag == 0:
            s += a[l]
            flag = 1
        else:
            d += a[l]
            flag = 0
        l = l + 1
    else:
        if flag == 0:
            s += a[r]
            flag = 1
        else:
            d += a[r]
            flag = 0
        r = r - 1

print(s, d)
