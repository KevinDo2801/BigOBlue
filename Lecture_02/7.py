n = int(input())
a = list(map(int, input().split()))

count = n
last_kill_pos = n - 1

for i in range(n - 1, -1, -1):
    last_kill_pos = min(last_kill_pos, i)
    current_kill_pos = max(0, i - a[i])

    if current_kill_pos < last_kill_pos:
        count -= (last_kill_pos - current_kill_pos)
        last_kill_pos = current_kill_pos


print(count)