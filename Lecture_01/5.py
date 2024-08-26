q = input()
w = input()
e = input()
t = input()

q = list(map(int, q.split()))
na = q[0]
nb = q[1]

w = list(map(int, w.split()))
k = w[0]
m = w[1]

a = list(map(int, e.split()))
b = list(map(int, t.split()))

ka = a[k - 1]
mb = b[len(b) - m]
if ka >= mb:
    print("NO")
else:
    print("YES")