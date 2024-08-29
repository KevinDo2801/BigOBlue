n, t = map(int, input().split())
a = list(map(int, input().split()))

start = 0
current_sum = 0
max_book = 0
for end in range(n):
    current_sum += a[end]

    while current_sum > t:
        current_sum -= a[start]
        start += 1
    
    max_book = max(max_book, end - start + 1)

print(max_book)