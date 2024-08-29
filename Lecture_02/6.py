n = int(input())
a = list(map(int, input().split()))

count = [0] * (10 ** 5 + 5)
diff = 0
start = 0
longest_range = 0

for end in range(n):
    if count[a[end]] == 0:
        diff += 1
    count[a[end]] += 1
    
    while start < end and diff > 2:
        count[a[start]] -= 1
        if count[a[start]] == 0:
            diff -= 1
        start += 1

    longest_range = max(longest_range, end - start + 1)

print(longest_range)