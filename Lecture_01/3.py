n = int(input())
a = list(map(int, input().split()))

prev_num = 0
for num in a:
    if num - prev_num > 15:
        print(prev_num + 15)
        break
    prev_num = num
else:
    print(min(a[-1] + 15, 90))
