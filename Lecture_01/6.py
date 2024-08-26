n = int(input())

index = -1
l, r = float('inf'), float('-inf')
arr = set()
for i in range(n):
    c = list(map(int, input().split()))
    a = c[0]
    b = c[1]
    arr.add((i, a, b))  # Add tuple (a, b) to the set

    if a < l:
        l = a
    if b > r:
        r = b

for e in arr:
    if e[1] == l and e[2] == r:
        print(e[0] + 1)
        break
else:
    print(-1)
