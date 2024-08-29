n, x = map(int, input().split())
c = list(map(int, input().split()))

c.sort()
h = 0
for i in range(n):
    h += x * c[i]
    if x != 1:
        x -= 1
    
print(h)
