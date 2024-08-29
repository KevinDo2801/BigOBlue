n = int(input())
a = list(map(int, input().split()))

count = max(1, n - a[n - 1]) 
last_kill_pos = max(0, n - a[n - 1])

for i in range(n - 2, -1, -1):
    current_kill_pos = max(0, i - a[i])
    if current_kill_pos == 0:
        break
    if current_kill_pos < last_kill_pos and last_kill_pos != n:
        count -= (last_kill_pos - current_kill_pos)
        last_kill_pos = current_kill_pos


print(count)