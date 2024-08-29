n, a, b = map(int, input().split())
h = list(map(int, input().split()))

h.sort()
start = h[b - 1]
end = h[b]
print(end - start)
