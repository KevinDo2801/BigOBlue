n = int(input())
a = list(map(int, input().split()))

b = sorted(a)

l = 0
r = n - 1
c = 0
d = 0
flag = 0

while l < r:
    if a[l] == b[l]:
        l += 1
    if a[r] == b[r]:
        r -= 1
    if a[l] != b[l] and a[r] != b[r]:
        if flag == 0:
            c = l + 1
            d = r + 1
            flag = 1
        if a[l] != b[r] or b[l] != a[r]:
            print("no")
            exit()
        l += 1
        r -= 1

print("yes")
if c == 0 and d == 0:
    print(1, 1)
else:
    print(c, d)
