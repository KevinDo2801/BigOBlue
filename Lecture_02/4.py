n, m, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = []
i = 0

for j in range(m): 
    while i < n and b[j] > a[i] + y: # tại sao lại chọn tối đa mà ko chọn từ đầu x
        i += 1
    
    if i == n:
        break

    if b[j] >= a[i] - x and b[j] <= a[i] + y:
        result.append((i + 1, j + 1))
        i += 1

print(len(result))
for pair in result:
    print(pair[0], pair[1])