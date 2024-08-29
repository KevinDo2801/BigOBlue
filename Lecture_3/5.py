n, w = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

cup_girl = a[0]
cup_boy = a[n]
x = cup_boy / 2
if x > cup_girl:
    x = cup_girl

total = 3 * n * x

if total > w:
    print(w)
else:
    print(total)





