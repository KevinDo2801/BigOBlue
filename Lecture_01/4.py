a = input()
c = input()

b = list(a)
i = len(a) - 1
while i >= 0:
    if b[i] < 'z':
        b[i] = chr(ord(b[i]) + 1)
        break
    b[i] = 'a'
    i -= 1

b = ''.join(b)

if b < c:
    print(b)
else:
    print("No such string")
