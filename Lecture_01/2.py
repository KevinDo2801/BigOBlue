a = input()
a = [ord(x) for x in a]

sum = 0
prev_num = 97
for num in a:
    sum += min((26 - abs(prev_num - num)), abs(prev_num - num))
    prev_num = num

print(sum)