a = input()
b = input()

s = {}
t = {}

for c in a:
    s[c] = s.get(c, 0) + 1

for c in b:
    t[c] = t.get(c, 0) + 1

    if c in s:
        t[c] -= 1
        s[c] -= 1
        if s[c] < 0:
            print("need tree")
            exit()

for c in b:
    if t[c] != 0:
        print("need tree")
        exit()

flag = True
for c in a:
    if s[c] != 0:
        flag = False
        break
if flag:
    print("array")
    exit()

i = 0
for c in a:
    if i < len(b) and c == b[i]:
        i += 1
    if i == len(b):
        print("automaton")
        exit()

print("both")
