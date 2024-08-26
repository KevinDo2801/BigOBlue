a = list(map(int, input().split()))
n = a[0]
k = a[1]

a.clear()
a = [0] * 101
for i in range(n):
    u = input()
    a[len(u)] += 1

cor = len(input())
time = 0
good_time = 0
bad_time = 0
m = k
for i in range(1, 101):
    if a[i] == 0:
        continue
    if cor == i:
        good_time = time + 1
        if a[i] >= m:
            time += (5 + m)
            a[i] -= m
            m = k   
        bad_time = time + (a[i] // m) * 5 + a[i]
        if a[i] % m == 0:
            bad_time -= 5
        break
    else:
        if a[i] >= m:
            time += (5 + m)
            a[i] -= m
            m = k
        time += (a[i] // m) * 5 + a[i]
        m -= a[i]

print(good_time, bad_time)