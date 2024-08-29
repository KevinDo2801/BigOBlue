n = int(input())
chocolate = list(map(int, input().split()))
t_alice = t_bob = 0
l, r = 0, n - 1

while l <= r:
    if t_alice + chocolate[l] <= t_bob + chocolate[r]:
        t_alice += chocolate[l]
        l += 1
    else:
        t_bob += chocolate[r]
        r -= 1

print(l, n - l)